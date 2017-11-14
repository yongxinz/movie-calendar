import config from "./utils/config";

App({
    //全局数据，中文日期，供转换用
    chineseDate: {
        years: ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九'],
        months: ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二']
    },
    config: config,
    onLaunch: function () {
    }
});