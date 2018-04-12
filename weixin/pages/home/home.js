const app = getApp();

Page({
    data: {
        gData: null,
        is_ready: false,
        results: {}
    },

    onLoad: function () {
        let that = this;

        app.helper.wxPromisify(wx.getUserInfo)().then(function (res) {
            app.config.gData.userInfo = res.userInfo;
            that.setData({'gData.userInfo': app.config.gData.userInfo, is_ready: true});
        }).catch(function (res) {
            wx.showModal({
                title: '微信授权',
                content: '为获得最佳体验，请按确定并在授权管理中选中“用户信息”，再重新进入小程序即可正常使用。',
                showCancel: false,
                success: function (res) {
                    if (res.confirm) {
                        wx.openSetting({
                            success: function success(res) {
                                console.log('openSetting success', res.authSetting);
                            }
                        });
                    }
                }
            })
        });
    },

    onShow: function () {
        // app.helper.waitUserSid(this.getApiData);
    }
});
