const app = getApp();

Page({
    data: {
        apiData: {},
        subject: '',
        buttonGo: '想看',
        buttonDone: '看过'
    },

    onLoad: function (options) {
        let that = this;
        that.setData({options: options, subject: options.subject});
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

            if (res.data.is_going) {
                that.setData({'buttonGo': '已想看'})
            } else {
                that.setData({'buttonGo': '想看'})
            }

            if (res.data.is_done) {
                that.setData({'buttonDone': '已看过'})
            } else {
                that.setData({'buttonDone': '看过'})
            }

            wx.hideLoading()
        })
    },

    movieTag: function (e) {
        let that = this;
        let type = e.currentTarget.dataset.type;

        app.helper.getApi('tag', {'subject': that.data.subject, 'type': type}).then(function (res) {
            if (res.data.results.Go) {
                that.setData({'buttonGo': '已想看'})
            } else {
                that.setData({'buttonGo': '想看'})
            }

            if (res.data.results.Done) {
                that.setData({'buttonDone': '已看过'})
            } else {
                that.setData({'buttonDone': '看过'})
            }
        })
    }
});
