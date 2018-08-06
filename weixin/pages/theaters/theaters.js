const app = getApp();

Page({
    data: {
        apiData: {}
    },

    onLoad: function (options) {

    },

    onShow: function () {
        app.helper.waitUserSid(this.getApiData);
    },

    getApiData: function () {
        let that = this;

        wx.showLoading({title: '加载中...'});
        app.helper.getApi('theaters').then(function (res) {
            that.setData({apiData: res.data});
        }).then(function () {
            wx.hideLoading()
        });
    }
});
