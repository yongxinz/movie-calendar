const app = getApp();

Page({
    data: {
        apiData: {},
        options: {
            page: 1
        },
        count: 0,
        msg: ''
    },

    onLoad: function (options) {
        this.setData({options: options});

        if (options.is_going === 'true') {
            wx.setNavigationBarTitle({
                title: '想看的电影'
            });
            this.setData({msg: '想看'});
        } else if (options.is_done === 'true') {
            wx.setNavigationBarTitle({
                title: '看过的电影'
            });
            this.setData({msg: '看过'});
        }
    },

    onShow: function () {
        app.helper.waitUserSid(this.getApiData);
    },

    getApiData: function () {
        let that = this;
        that.setData({
            'options.page': 1
        });

        wx.showLoading({title: '加载中...'});
        app.helper.getApi('retain', that.data.options).then(function (res) {
            that.setData({apiData: res.data});
            that.setData({count: res.data.count});
        }).then(function () {
            wx.hideLoading()
        });
    },

    onReachBottom: function () {
        let that = this;
        if (that.data.apiData.next !== null) {
            let next_page = that.data.options.page + 1;
            that.setData({
                'options.page': next_page
            });

            wx.showLoading({title: '加载中...'});
            app.helper.getApi('retain', that.data.options).then(function (res) {
                for (let i = 0; i < res.data.results.length; i++) {
                    that.data.apiData.results.push(res.data.results[i])
                }
                that.setData({apiData: that.data.apiData, 'apiData.next': res.data.next});
            }).then(function () {
                wx.hideLoading()
            });
        }
    }
});
