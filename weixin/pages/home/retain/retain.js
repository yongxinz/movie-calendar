const app = getApp();

Page({
    data: {
        apiData: {},
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

        app.helper.getApi('retain', that.data.options).then(function (res) {
            that.setData({apiData: res.data.results});
            that.setData({count: res.data.count});
        })
    }
});
