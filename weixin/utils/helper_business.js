let config = require('./config');

function wxPromisify(fn) {
    return function (obj = {}) {
        return new Promise((resolve, reject) => {
            obj.success = function (res) {
                resolve(res)
            };

            obj.fail = function (res) {
                reject(res)
            };

            fn(obj)
        })
    }
}

function waitSomething(fn, st) {
    if (config.gData[st]) {
        fn();
    } else {
        config.emitter.on(st, fn);
    }
}

function get_api_url_name(api_name) {
    return config.baseURL + config.apiMap[api_name]
}

function requestApi(api_name, data, uri = '', method = 'GET') {
    return new Promise((resolve, reject) => {
        // console.log(get_api_url_name(api_name) + uri);
        wxPromisify(wx.request)({
            url: get_api_url_name(api_name) + uri,
            header: { 'Authorization': config.gData.userSid },
            data: data,
            method: method,
        }).then(function (res) {
            if (res.statusCode === 403) {
                wx.navigateTo({url: '/pages/login/login'})
            } else {
                resolve(res)
            }
        }).catch(function (res) {
            reject(res);
        });
    })
}

module.exports.getUrl = function (api_name) { 
    return get_api_url_name(api_name)
};

module.exports.waitUserSid = function (fn) {
    return waitSomething(fn, 'userSid')
};

module.exports.waitUserInfo = function (fn) {
    return waitSomething(fn, 'userInfo')
};

module.exports.getApi = function (api_name, data, uri = '') {
    return requestApi(api_name, data, uri, 'GET')
};

module.exports.postApi = function (api_name, data, uri = '') {
    return requestApi(api_name, data, uri, 'POST')
};

module.exports.putApi = function (api_name, data, uri = '') {
    return requestApi(api_name, data, uri, 'PUT')
};

module.exports.deleteApi = function (api_name, data, uri = '') {
    return requestApi(api_name, data, uri, 'DELETE')
};

module.exports.checkJoin = function () {
    return new Promise((resolve, reject) => {
        this.getApi('check').then(function (res) {
            if (res.data.status === true) {
                resolve(res)
            } else {
                if (res.data.code === 403001) {
                    // 情况少见，需要重新打开小程序或走微信验证程序
                    console.log(res.data.code)
                }

                if (res.data.code === 403002) {
                    wx.navigateTo({url: '/pages/login/login'})
                }
            }
        });
    })
};

module.exports.wxPromisify = wxPromisify;

class Router {
    navigateBack(obj) {
        let delta = obj.delta ? obj.delta : 1;

        if (obj.data) {
            let pages = getCurrentPages()
            let curPage = pages[pages.length - (delta + 1)];
            if (curPage.pageForResult) {
                curPage.pageForResult(obj.data);
            } else {
                curPage.setData(obj.data);
            }
        }
        wx.navigateBack({
            delta: delta, // 回退前 delta(默认为1) 页面
            success: function (res) {
                // success
                obj.success && obj.success(res);
            },
            fail: function (err) {
                // fail
                obj.function && obj.function(err);
            },
            complete: function () {
                // complete
                obj.complete && obj.complete();
            }
        })
    }
}

module.exports.Router = new Router();

module.exports.setToast = function (that, message) {
    that.setData({
        toastMessage: message
    });
    setTimeout(function () {
        that.setData({
            toastMessage: ''
        })
    }, 1500)
};
