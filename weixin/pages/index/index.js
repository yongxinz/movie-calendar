var wezrender = require('../../utils/wezrender.min.js');

var app = getApp();

Page({
    data: {
        windowWidth: 0,
        windowHeight: 0,
        current: 14,
        index: 14,
        id: '',
        is_today: false,
        apiData: {id: ''}
    },

    onLoad: function (options) {
        if (options.id !== undefined) {
            this.setData({id: options.id});
        }

        let that = this;
        wx.getSystemInfo({
            success: function (res) {
                that.setData({
                    windowWidth: res.windowWidth,
                    windowHeight: res.windowHeight
                });
            }
        });

        var zr = wezrender.zrender.init("line-canvas-1", 375, 600);
        var circle = new wezrender.graphic.Image({
            'style': {
                x: 0,
                y: 0,
                image: '../../static/image/full-star.png',
                width: 32,
                height: 24,
                text: 'koala'
            }
        });
        zr.add(circle);

        this.showDate(new Date());
        app.helper.waitUserSid(this.getApiData);
    },

    onShow: function () {

    },

    showDate: function (day) {
        var today = day, _this = this, year = today.getFullYear() + '', i = 0, chineseYear = '',
            week = today.getDay();

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

        _this.setData({
            'year': chineseYear,
            'month': app.chineseDate.months[today.getMonth()],
            'day': today.getDate(),
            'week': week_
        })
    },

    getApiData: function () {
        let that = this;

        wx.showLoading({ title: '加载中...' });
        app.helper.getApi('movie', {'id': that.data.id}).then(function (res) {
            that.setData({apiData: res.data.results});
            wx.hideLoading();
        })
    },

    bindChange: function (e) {
        var before = new Date()-1000*60*60*24*(this.data.current-e.detail.current);
        var beforeDate = new Date(before);

        if (beforeDate - new Date() !== 0) {
            this.setData({is_today: true, index: e.detail.current});
        } else {
            this.setData({is_today: false, index: e.detail.current});
        }

        this.showDate(beforeDate);
    },

    onShareAppMessage: function () {
        return {
            title: this.data.apiData[this.data.index].title,
            path: '/pages/index/index?id=' + this.data.apiData[this.data.index].id
        }
    },

    movieDetail: function (e) {
        let subject = e.currentTarget.dataset.subject;
        wx.navigateTo({url: '../detail/detail?subject=' + subject })
    }
});
