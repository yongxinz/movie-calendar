const app = getApp();

Page({
    data: {
        gData: null,
        results: {}
    },

    onLoad: function () {
        let that = this;

        app.helper.wxPromisify(wx.getUserInfo)().then(function (res) {
            app.config.gData.userInfo = res.userInfo;
            that.setData({'gData.userInfo': app.config.gData.userInfo});
        });
    },

    onShow: function () {
        // app.helper.waitUserSid(this.getApiData);
    },

    // 获取用户头像昵称
    bindGetUserinfo: function (res) {
        this.setData({'gData.userInfo': res.detail.userInfo})
    }
});
