const app = getApp();

Page({
    data: {
        filminfo: "",
        filmgenres: "",
        filmcountry: "",
        filmcast: ""
    },

    onLoad: function (options) {
        let that = this;
        that.setData({options: options});
    },

    onShow: function () {
        this.getApiData();
    },

    getApiData: function () {
        let that = this;

        wx.showLoading({ title: '加载中...' });
        app.helper.getApi('detail', that.data.options).then(function (res) {
            console.log(res)

            var data = res.data;
            console.log(data);
            // data.directors.map(function(item){
            //  return item + "(导演)";

            var directors = [];
            var casts = [];
            if (data.rating.average >= 9.5) {
                data.rating.star = "star10";
            } else {
                data.rating.star = "star" + Math.round(data.rating.average);
            }
            for (var item in data.directors) {
                console.log(item);
                directors.push(data.directors[item].name + "(导演) ");
            }
            console.log(data);
            for (var item in data.casts) {
                console.log(item);
                casts.push(" " + data.casts[item].name + " ");
            }
            that.setData({
                filminfo: data,
                filmgenres: data.genres.join(" / "),
                filmcountry: data.countries.join(" / "),
                filmcast: directors.join("/") + "/" + casts.join("/")
            })
        })
    }
});
