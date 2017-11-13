var wezrender = require('../../utils/wezrender.min.js')

var app = getApp();

Page({
    data: {
        'year': 0,
        'month': 0,
        'day': 0,
        'week': 0,
        'show_year': 0,
        'directors': '',
        'title': '',
        'average': '',
        'stars': '',
        'loading_opacity': 1,
        'animationData': '',
        'images': '',
        'casts': '',
        'start': undefined
    },

    // 页面初始化
    onLoad: function (options) {
        this.setData({ start: options.start })

        var zr = wezrender.zrender.init("line-canvas-1", 375, 600);
        var circle = new wezrender.graphic.Image({
            'style': {
                x: 0,
                y: 0,
                image: '../../image/full-star.png',
                width: 32,
                height: 24,
                text: 'koala'
            }
        });
        zr.add(circle);
    },

    //页面初次渲染完成
    onReady: function (e) {
        this.showDate();
        this.loadMovie();
    },

    //显示日期，年月日
    showDate: function () {
        var today = new Date(), _this = this, year = today.getFullYear() + '', i = 0, chineseYear = '',
            week = today.getDay();
        //将年份转换为中文
        do {
            chineseYear = chineseYear + app.chineseDate.years[year.charAt(i)];
            i++;
        } while (i < year.length);

        var week_ = '';
        if (week === 0) {
            week_ = '日'
        } else {
            week_ = app.chineseDate.years[week]
        }
        //设置数据
        _this.setData({
            'year': chineseYear,
            'month': app.chineseDate.months[today.getMonth()],
            'day': today.getDate(),
            'week': week_
        })
    },

    //加载top250电影信息
    loadMovie: function () {
        if (this.data.start === undefined) {
            this.setData({ start: Math.floor(Math.random() * 250) });
        }
        
        var _this = this,
            //请求发送的数据，随机的起始值和条数（只需要一条）
            reqData = {
                start: _this.data.start,
                count: 1
            };

        wx.request({
            url: 'https://api.douban.com/v2/movie/top250',
            data: reqData,
            header: {
                'Content-Type': 'json'
            },
            success: function (res) {
                var movieData = res.data.subjects[0];
                wx.request({
                    url: movieData.alt + '/comments',
                    header: {
                        'Content-Type': 'json'
                    },
                    success: function (res) {
                        var comment = res.data.match(/<\s*p\s+class=""\s*>(.*?)[\n\r\t]+/g);

                        var directors = '';
                        var casts = '';
                        for (var i in movieData.directors) {
                            directors += movieData.directors[i].name + '/'
                        }

                        for (var i in movieData.casts) {
                            casts += movieData.casts[i].name + '/'
                        }

                        //设置数据，评分是整数需要补上小数点和0
                        var average = movieData.rating.average % 1 === 0 ? movieData.rating.average + '.0' : movieData.rating.average;
                        var renderData = {
                            'show_year': movieData.year,
                            'directors': directors,
                            'title': movieData.title,
                            'comment': comment[1].slice(12),
                            'average': average,
                            'stars': _this.starCount(movieData.rating.stars),
                            'loading_opacity': 0,
                            'images': movieData.images.large,
                            'casts': casts
                        };
                        _this.setData(renderData);
                        _this.loading();
                    }
                })
            }
        });
    },

    //计算行星显示规则
    starCount: function (originStars) {
        //计算星星显示需要的数据，用数组stars存储五个值，分别对应每个位置的星星是全星、半星还是空星
        var starNum = originStars / 10, stars = [], i = 0;
        do {
            if (starNum >= 1) {
                stars[i] = 'full';
            } else if (starNum >= 0.5) {
                stars[i] = 'half';
            } else {
                stars[i] = 'no';
            }
            starNum--;
            i++;
        } while (i < 5);

        return stars;
    },

    //加载动画
    loading: function () {
        var animation = wx.createAnimation({
            duration: 1000,
            timingFunction: 'ease'
        });
        animation.opacity(1).step();
        this.setData({
            animationData: animation.export()
        })
    },

    onShareAppMessage: function () {
        return {
            title: this.data.title,
            path: '/pages/index/index?start=' + this.data.start + '&count=1'
        }
    }
});
