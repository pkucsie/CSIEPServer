(function (c) { $type = String; $type.__typeName = "String"; $type.__class = true; $prototype = $type.prototype; $prototype.endsWith = function g(i) { return (this.substr(this.length - i.length) === i) }; $prototype.startsWith = function e(i) { return (this.substr(0, i.length) === i) }; $prototype.trim = function f() { return this.replace(/^\s+|\s+$/g, "") }; $prototype.trimEnd = function b() { return this.replace(/\s+$/, "") }; $prototype.trimStart = function h() { return this.replace(/^\s+/, "") }; $type.format = function a(j, i) { return String._toFormattedString(false, arguments) }; $type._toFormattedString = function d(n, o) { var u = ""; var p = o[0]; for (var k = 0; ;) { var l = p.indexOf("{", k); var s = p.indexOf("}", k); if ((l < 0) && (s < 0)) { u += p.slice(k); break } if ((s > 0) && ((s < l) || (l < 0))) { if (p.charAt(s + 1) !== "}") { throw new Error("format stringFormatBraceMismatch") } u += p.slice(k, s + 1); k = s + 2; continue } u += p.slice(k, l); k = l + 1; if (p.charAt(k) === "{") { u += "{"; k++; continue } if (s < 0) { throw new Error("format stringFormatBraceMismatch") } var t = p.substring(k, s); var m = t.indexOf(":"); var q = parseInt((m < 0) ? t : t.substring(0, m), 10) + 1; if (isNaN(q)) { throw new Error("format stringFormatInvalid") } var j = (m < 0) ? "" : t.substring(m + 1); var r = o[q]; if (typeof (r) === "undefined" || r === null) { r = "" } if (r.toFormattedString) { u += r.toFormattedString(j) } else { if (n && r.localeFormat) { u += r.localeFormat(j) } else { if (r.format) { u += r.format(j) } else { u += r.toString() } } } k = s + 1 } return u } })(window);
$.extend($.fn, {
    validate: function (options) {
        var validation = new $.validator(options, this[0]);
        return validation;
    },
    checkUInput: function () {
        return $.validator.check();
    }
});

$.validator = function (options, form) {
    //setTimeout(function (options, form) { $.validator.prototype.init(options, form) }, 1000);
    this.init(options, form);
};
$.extend($.validator, {
    bind: function (options, form) {
        //添加系统默认值
        $.validator.currentForm = $(form);
        $.validator.submitbtn = $.validator.currentForm.find(".submit");
        $.validator.errorclass = options.errorclass ? options.errorclass : "error-info";
        $.validator.succeedclass = options.succeedclass ? options.succeedclass : "success-info";
        $.validator.errordiv = options.errordiv ? options.errordiv : "error_div";
        $.validator.btnmsg = options.btnmsg ? options.btnmsg : "正在执行，请稍候...";
        $.validator.beforesubmit = options.beforesubmit;
        $.validator.beforecheck = options.beforecheck;
        var showerror = true;
        if (options.showErrormsg !== undefined) {
            showerror = options.showErrormsg;
        }
        $.validator.showErrormsg = showerror;
        var showallerror = true;
        if (options.showallerror !== undefined) {
            showallerror = options.showallerror;
        }
        $.validator.showallerror = showallerror;
    },
    messages: {
        c: "此项不能为空，请填写！",
        email: "请填写正确格式的邮箱",
        l: "请填写内容长度 在 {0} 和 {1} 个字符内！",
        v: "请填写数值大小在 {0} 和 {1}之间！",
        d: "请填写数字！",
        dint: "请填写整数！",
        url: "请填写有效的Url地址",
        date: "请填写有效的日期",
        equalTo: "两次输入不一样，请再次输入！",
        mobile: "请填写正确格式的手机号",
        mobileorphone: "请填写正确格式的电话号码",
        tel: "请输入正确格式的电话号码",
        r: "输入有误，请检查！",
        decimal: "请输入正确数字"
    },
    check: function (elelist) {
        var form = this.currentForm;
        var errorclass = this.errorclass;
        if (!this.showErrormsg) {
            errorclass = "has-error";
        }
        if (this.beforecheck) {
            if (!this.beforecheck.call(this, form)) {
            }
        }
        if (elelist) {
            elelist.trigger("blur");
        } else {
            var t = form.find("*[data-rules]").not(':hidden');
            !!t && t.trigger("blur");
        }
        if (this.beforesubmit) {
            if (!this.beforesubmit.call(this, form)) {
                return false;
            }
        }
        var error = form.find("." + errorclass);
        $.validator.firsterror = '';
        if (error.length > 0) $.validator.firsterror = error[0];
        return form.find("." + errorclass).not(':hidden').length <= 0;
    },
    haserror: function (element) {
        var form = this.currentForm;
        var errorclass = this.errorclass;
        if (!this.showErrormsg) {
            errorclass = "has-error";
        }
        var error = form.find("." + errorclass);
        if (error.length < 1) return false;
        if (error.length > 1) return true;
        return !element.closest('.form-group').hasClass(errorclass);
    },
    optional: function (element) {
        var val = this.elementValue(element);
        return !$.validator.methods.required.call(this, val, element) && "dependency-mismatch";
    },
    elementValue: function (element) {
        var val,
            $element = $(element),
            type = element.type;

        if (type === "radio" || type === "checkbox") {
            return this.findByName(element.name).filter(":checked").val();
        } else if (type === "number" && typeof element.validity !== "undefined") {
            return element.validity.badInput ? false : $element.val();
        }

        val = $element.val();
        if (typeof val === "string") {
            return val.replace(/\r/g, "");
        }
        return val;
    },
    depend: function (param, element) {
        return this.dependTypes[typeof param] ? this.dependTypes[typeof param](param, element) : true;
    },
    dependTypes: {
        "boolean": function (param) {
            return param;
        },
        "string": function (param, element) {
            return !!$(param, element.form).length;
        },
        "function": function (param, element) {
            return param(element);
        }
    },
    checkable: function (element) {
        return (/radio|checkbox/i).test(element.type);
    },
    getLength: function (value, element) {
        if (!value) {
            return 0;
        }
        if (element && element.nodeName) {
            switch (element.nodeName.toLowerCase()) {
                case "select":
                    return $("option:selected", element).length;
                case "input":
                    if (this.checkable(element)) {
                        return this.findByName(element.name).filter(":checked").length;
                    }
            }
        }
        return value.length;
    },
    findByName: function (name) {
        return $(this.currentForm).find("[name='" + name + "']");
    },
    CheckCanNull: function (value, element, cannull) {
        var len = $.isArray(value) ? value.length : $.validator.getLength($.trim(value), element);
        if (cannull === 'true' && len < 1)
            return true;
        return false;
    },
    addMethod: function (name, method) {
        $.validator.methods[name] = method;
    },
    methods: {
        //判断是否为空
        c: function (value, element) {
            if (element.nodeName.toLowerCase() === "select") {
                var val = $(element).val();
                if (!val) return false;
                return val.length > 0;
            }
            if ($.validator.checkable(element)) {
                return $.validator.getLength(value, element) > 0;
            }
            return value.length > 0;
        },
        //判断邮箱格式
        email: function (value, element, param, error, cannull) {
            value = $.trim(value);
            if ($.validator.CheckCanNull(value, element, cannull)) {
                return true;
            }
            return /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/.test(value);
        },
        //判断输入字段长度
        l: function (value, element, param, error, cannull) {
            value = $.trim(value);
            var len = $.isArray(value) ? value.length : $.validator.getLength($.trim(value), element);
            if (cannull === 'true' && len < 1) {
                return true;
            }
            var reg = /^{(\d+)?,(\d+)?}$/;
            param = reg.exec(param);
            var minl = param[1];
            var maxl = param[2];
            if (minl > 0 && maxl > 0) {
                return (len >= minl && len <= maxl) ? true : String.format(error, minl, maxl);
            } else if (minl == undefined) {
                return len <= maxl ? true : String.format(error, maxl);
            } else if (maxl == undefined) {
                return len >= minl ? true : String.format(error, minl);
            }
            return true;
        },
        //判断输入字段取值范围
        v: function (value, element, param, error, cannull) {
            if ($.validator.CheckCanNull(value, element, cannull)) {
                return true;
            }
            var reg = /^{(\d+)?,(\d+)?}$/;
            param = reg.exec(param);
            var minv = param[1];
            var maxv = param[2];
            if (minv > 0 && maxv > 0) {
                return (value >= minv && value <= maxv) ? true : String.format(error, minv, maxv);
            } else if (minv == undefined) {
                return value <= maxv ? true : String.format(error, maxv);
            } else if (maxv == undefined) {
                return value >= minv ? true : String.format(error, minv);
            }
            return true;
        },

        d: function (value, element, param, error, cannull) {
            if ($.validator.CheckCanNull(value, element, cannull)) {
                return true;
            }
            if (value > nowtime()) {
                return false;
            }
            var reg = /^[1-9]\d*$/;
            //param = reg.exec(param);
            return reg.test(value);
        },
        dint: function (value, element, param, error, cannull) {
            //if ($.validator.CheckCanNull(value, element, cannull)) {
            //    return true;
            //}
            var reg = /^\+?[1-9]([0-9])*$/;
            return reg.test(value);
        },
        decimal: function (value, element, param, error, cannull) {
            //if ($.validator.CheckCanNull(value, element, cannull)) {
            //    return true;
            //}
            var reg = /^\d+(\.\d+)?$/;
            return reg.test(value);
        },
        //判断是否为URL链接
        url: function (value, element, param, error, cannull) {
            value = $.trim(value);
            if ($.validator.CheckCanNull(value, element, cannull)) {
                return true;
            }
            return /^(https?|s?ftp):\/\/(((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:)*@)?(((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))|((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?)(:\d*)?)(\/((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)+(\/(([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)*)*)?)?(\?((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|[\uE000-\uF8FF]|\/|\?)*)?(#((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|\/|\?)*)?$/i.test(value);
        },
        //判断是否为日期格式
        date: function (value, element, param, error, cannull) {
            value = $.trim(value);
            if ($.validator.CheckCanNull(value, element, cannull)) {
                return true;
            }
            return !/Invalid|NaN/.test(new Date(value).toString());
        },
        //判断值是否相等
        equalTo: function (value, element, param) {
            var ele = $(param);
            return value === $.trim(ele.val());
        },
        //判断是否为手机号
        mobile: function (value, element, param, error, cannull) {
            value = $.trim(value);
            if ($.validator.CheckCanNull(value, element, cannull)) {
                return true;
            }
            return /^1\d{10}$/.test(value);
        },
        //判断是否为手机号或电话
        mobileorphone: function (value, element, param, error, cannull) {
            value = $.trim(value);
            if ($.validator.CheckCanNull(value, element, cannull)) {
                return true;
            }
            var mobile = /^1\d{10}$/;
            var tel = /^(\d{3,4}-?)?\d{7,9}(-\d{3,4})?$/;
            return (tel.test(value) || mobile.test(value));
        },
        //判断是否为电话
        tel: function (value, element, param, error, cannull) {
            value = $.trim(value);
            if ($.validator.CheckCanNull(value, element, cannull)) {
                return true;
            }
            var tel = /^\d{3,4}-?\d{7,9}$/;
            return tel.test(value);
        },
        r: function (value, element, param, error, cannull) {
            return param.test($.trim(value));
        }
    },
    //通过验证，Post提交
    submit: function (options) {
        var currentForm = this.currentForm;
        //var currentForm = $.validator.currentForm;
        var errordiv = this.errordiv;
        var btn = this.submitbtn;
        var btndfault = btn.val();
        btn.val(options.btnmsg).attr("disabled", "disabled");
        var errordivcon = currentForm.find("#" + errordiv);
        if (errordivcon) errordivcon.html("");
        var showProgress = true;
        if (options.ShowProgress != undefined) {
            showProgress = options.ShowProgress;
        }
        if (showProgress && $.loading) $.loading();
        $.ajax({
            type: "post",
            url: currentForm.attr("action"),
            data: currentForm.serialize().replace(/%3C/g, "%26lt%3B").replace(/%3E/g, "%26gt%3B"),
            success: function (data) {
                btn.val(btndfault).removeAttr("disabled");
                if (showProgress && $.removeloading) $.removeloading();
                if (options.showResult) {
                    if (!options.showResult.call(this, data)) {
                        return false;
                    }
                } else {
                    $.validator.showResult(data, errordivcon);
                }
                if (options.aftersubmit) {
                    if (!options.aftersubmit.call(this, data)) {
                        return false;
                    }
                }
                return false;
            },
            error: function () {
                if (showProgress && $.removeloading) $.removeloading();
                btn.val(btndfault).removeAttr("disabled");
            }
        });
    },
    showResult: function (data, lResult) {
        if (lResult) {
            if (data.code == 1) {
                //lResult.html(data.msg);
                //gDialog.fAlert(data.msg);
            } else {
                lResult.html("<i class=\"fa fa-exclamation-triangle\"></i> " + data.msg);
            }
        }
    },
    adderror: function (element, errorcontent, showerror) {
        element = $(element);
        this.clean(element);
        var formgroup = element.closest(".form-group");
        var errorclass = this.errorclass;
        formgroup.addClass("has-error");
        if (!$.validator.showErrormsg) return;
        var error = "<span class=\"" + errorclass + "\">" + errorcontent + "</span>";
        if (formgroup.find(".radio-list").length > 0 || formgroup.find(".checkbox-list").length > 0) {
            formgroup.append(error);
        } else {
            var inputgroup = element.parent(".input-group");
            if (inputgroup.length > 0) {
                inputgroup.parent().append(error);
            } else {
                element.parent().append(error);
            }
        }
    },
    addsucceed: function (element) {
        this.clean(element);
        $(element).closest(".form-group").removeClass("has-error");
    },
    clean: function (element) {
        var errorclass = $.validator.errorclass;
        var succeedclass = $.validator.succeedclass;
        var $parent = $(element).closest(".form-group");
        $parent.find("." + errorclass).remove();
        $parent.find("." + succeedclass).remove();
    },
    showres: function (errcontent, element, result, showerror) {
        var r = true;
        try {
            if (!$.validator.showErrormsg) showerror = true;
            if (result == null || result === undefined) {
                result = "";
            }
            if (typeof result == "boolean") {
                if (result) {
                    $.validator.addsucceed(element);
                } else {
                    $.validator.adderror(element, errcontent, showerror);
                    r = false;
                }
            } else {
                $.validator.adderror(element, result);
                r = false;
            }
        } catch (j) {
            r = false;
        }
        return r;
    },
    prototype: {
        init: function (options, form) {
            $.validator.bind(options, form);
            var form = $.validator.currentForm;
            var inputlist = form.find("*[data-rules]");//.not(':hidden'); //$('#'+ formid + " :input.required");
            form.find("*[data-rules]").unbind("blur").unbind("keyup").unbind("focus");
            inputlist.blur(function () {
                var element = $(this);
                if (!$.validator.showallerror && $.validator.haserror(element)) {
                    return;
                }
                var tip = $(this).closest(".form-group").find(".help-block");
                if (tip)
                    if (tip.length > 0) {
                        tip.addClass("hide");
                    }

                var rules = element.data("rules");
                if (rules == "") {
                    rules = "c";
                }
                rules = rules.split(";");
                var val = $.validator.elementValue(element);
                var r1 = "", r2 = "", r3 = "", r4 = false;
                for (var key in rules) {
                    if (rules.hasOwnProperty(key)) {
                        var rule = rules[key].split(":");
                        //获取单个rule规则
                        r1 = rule[0];
                        //正则验证
                        if (r1 == "r") {
                            if (rule.length > 1) {
                                r2 = new RegExp(rule[1]);
                                if (rule.length === 2) {
                                    r3 = $.validator.messages[r1];
                                } else {
                                    r3 = rule[2];
                                    if (rule.length > 3)
                                        r4 = rule[3];
                                }
                                if (r2.test($.trim(val))) {
                                    $.validator.addsucceed(element);
                                } else {
                                    $.validator.adderror(element, r3);
                                    break;
                                }
                            }
                        } else {
                            if (rule.length === 1) {
                                if ($.validator.messages.hasOwnProperty(r1)) {
                                    r3 = $.validator.messages[r1];
                                }
                            } else if (rule.length === 2) {
                                r2 = rule[1];
                                if ($.validator.messages.hasOwnProperty(r1)) {
                                    r3 = $.validator.messages[r1];
                                }
                            } else {
                                r2 = rule[1];
                                r3 = rule[2];
                                if (rule.length > 3) {
                                    r4 = rule[3];
                                }
                            }
                            var result = $.validator.methods[r1].call(this, val, element[0], r2, r3, r4);
                            if (!$.validator.showres(r3, element, result, options.showerror)) {
                                break;
                            }
                        }
                    }
                } //循环结束
            }).focus(function () {
                $.validator.addsucceed(this);
                var tip = $(this).closest(".form-group").find(".help-block");
                if (tip)
                    if (tip.length > 0) {
                        tip.removeClass("hide");
                    }
                //$(this).triggerHandler("blur");
            }); //end blur

            var $submit = form.find(".submit"); //$(formid + " .submit");
            if ($submit.length > 0) {
                $submit.unbind('click').click(function () {
                    if ($.validator.check()) {
                        $.validator.bind(options, form);
                        $.validator.submit(options);
                    } else if ($('.layui-layer').length < 1 && $.validator.firsterror !== '' && $.validator.firsterror != undefined) {
                        var error = $($.validator.firsterror);
                        var scrollOffset = error.offset();
                        if (error.closest(".form-group").length > 0) {
                            scrollOffset = error.closest(".form-group").offset();
                        }
                        $("body,html").animate({
                            scrollTop: scrollOffset.top
                        }, 300);
                    }
                });
            }
        },
        getrules: function (element) {
            if (element) return $(element).data("rules");
            return null;
        },
        geterrors: function (element) {
            if (element) {
                return $(element).data("errors");
            }
            return null;
        }
    }
});
function nowtime() {//将当前时间转换成yyyymmdd格式
    var mydate = new Date();
    var str = "" + mydate.getFullYear();
    var mm = mydate.getMonth() + 1
    if (mydate.getMonth() > 9) {
        str += mm;
    }
    else {
        str += "0" + mm;
    }
    if (mydate.getDate() > 9) {
        str += mydate.getDate();
    }
    else {
        str += "0" + mydate.getDate();
    }
    return str;
}