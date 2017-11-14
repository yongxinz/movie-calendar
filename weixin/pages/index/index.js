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
        'rating': '',
        'stars': '',
        'loading_opacity': 1,
        'animationData': '',
        'images': '',
        'casts': '',
        'id': ''
    },

    // 页面初始化
    onLoad: function (options) {
        if (options.id !== undefined) {
            this.setData({ id: options.id });
        }

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

    onShow: function () {
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

    loadMovie: function () {
        let that = this;
        wx.request({
            url: app.config.api.movie,
            data: {'id': that.data.id},
            header: {
                'Content-Type': 'json'
            },
            success: function (res) {
                let movieData = res.data[0];
                let renderData = {
                    'show_year': movieData.year,
                    'directors': movieData.directors,
                    'title': movieData.title,
                    'comment': movieData.comment,
                    'rating': movieData.rating,
                    'stars': that.starCount(movieData.stars),
                    'images': movieData.images,
                    'casts': movieData.casts,
                    'loading_opacity': 0
                };
                that.setData(renderData);
                that.loading();
            }
        })
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
            path: '/pages/index/index?id=' + this.data.id
        }
    }
});
