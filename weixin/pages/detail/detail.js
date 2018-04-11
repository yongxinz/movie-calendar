const app = getApp();

Page({
    data: {
        apiData: {}
    },

    onLoad: function (options) {
        let that = this;
        that.setData({options: options});
    },

    onShow: function () {
        app.helper.waitUserSid(this.getApiData)
    },

    getApiData: function () {
        let that = this;

        wx.showLoading({ title: '加载中...' });
        app.helper.getApi('detail', that.data.options).then(function (res) {
            let directors = [];
            let casts = [];
            for (let m in res.data.directors) {
                directors.push(res.data.directors[m].name + '(导演) ')
            }
            for (let m in res.data.casts) {
                casts.push(res.data.casts[m].name)
            }
            res.data.directors = directors;
            res.data.casts = casts;

            if (res.data.rating.average >= 9.5) {
                res.data.rating.star = 'star10'
            } else {
                res.data.rating.star = 'star' + Math.round(res.data.rating.average)
            }

            that.setData({apiData: res.data});
            wx.hideLoading()
        })
    }
});
