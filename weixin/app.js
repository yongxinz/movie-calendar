const helperB = require('./utils/helper_business');
const configB = require('./utils/config');

App({
    //全局数据，中文日期，供转换用
    chineseDate: {
        years: ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九'],
        months: ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二']
    },
    config: configB,
    helper: helperB,

    onLaunch: function () {
        this.wxLogin();
        this.wxUserInfo();
    },

    wxLogin: function () {
        // 微信登录，获取用户code
        helperB.wxPromisify(wx.login)().then(function (res) {
            // 登录后端, wx code -> dj sid
            helperB.getApi('login', {code: res.code}).then(function (res) {
                configB.gData.userSid = res.data.sid;
                configB.emitter.emit('userSid');
            });
        }).catch(function (res) {
            console.error(res.errMsg)
        });
    },

    wxUserInfo: function () {
        // 获取用户基础信息
        helperB.wxPromisify(wx.getSetting)().then(function (res) {
            if (res.authSetting['scope.userInfo']) {
                helperB.wxPromisify(wx.getUserInfo)().then(function (res) {
                    configB.gData.userInfo = res.userInfo;
                    configB.emitter.emit('userInfo');
                }).catch(function (res) {
                    console.error(res.errMsg)
                });
            }
        });
    }
});
