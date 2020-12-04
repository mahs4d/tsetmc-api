var ColDefault = {
    ColTitle: "",
    ColData: "",
    ColAlign: "",
    ColColor: "",
    ColStyle: "",
    ColWidth: "100",
    ColBackground: "",
    ColBorder: ""
};
var TemplateStyle = [["", "Normal"], ["font-weight:bold", "Bold"], ["font-style:italic", "Italic"], ["font-style:italic;font-weight:bold", "Bold-Italic"]];
var TemplateBorder = [["", "بدون خط"], ["border-left:1px solid black", "سمت چپ"], ["border-left:1px solid black", "سمت راست"], ["border-left:1px solid black;border-right:1px solid black", "هر دو طرف"]];
var TemplateColor = [["#000000", "سیاه"], ["#990000", "قرمز"], ["#000099", "آبی"], ["#999900", "#999900"], ["#990099", "#990099"], ["#009999", "#009999"], ["#009900", "سبز"]];
var TemplateBackground = [["", "---"], ["rgba(255,212,212,0.5)", "قرمز"], ["rgba(212,212,255,0.5)", "آبی"], ["rgba(212,255,212,0.5)", "سبز"]];
+".t0c2{background-color:;}.t0c3{background-color:;}.t0c4{background-color:;}";
var TemplateAlign = [["left", "چپ چین"], ["center", "وسط چین"], ["right", "راست چین"]];
var TemplateData = [["l18", "نماد", 50], ["l30", "نام", 140], ["l", "نماد و نام", 170], ["tno", "تعداد معامله", 40], ["tvol", "حجم معامله", 70], ["tval", "ارزش معامله", 70], ["py", "قیمت دیروز", 50], ["pf", "اولین قیمت", 50], ["pmin", "کمترین قیمت", 50], ["pmax", "بیشترین قیمت", 50], ["pl", "آخرین قیمت", 50], ["plc", "آخرین قیمت - تغییر", 35], ["plp", "آخرین قیمت - درصد", 35], ["pc", "قیمت پایانی", 50], ["pcc", "قیمت پایانی - تغییر", 35], ["pcp", "قیمت پایانی - درصد", 35], ["eps", "EPS", 35], ["pe", "P/E", 35], ["pd1", "قیمت خرید", 40], ["zd1", "تعداد خریدار", 50], ["qd1", "حجم خرید", 50], ["po1", "قیمت فروش", 40], ["zo1", "تعداد فروشنده", 50], ["qo1", "حجم فروش", 50], ["cfield0", "cfield0", 50], ["cfield1", "cfield1", 50], ["cfield2", "cfield2", 50]];
var MWTemplates = [{
    title: "جدول کلاسیک",
    all: '<style>.t0head{cursor:pointer;border:0px solid #eeeeee;font-size:11px;direction:ltr;text-align:left;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c{border:0px solid #ffffff;font-size:11px;direction:ltr;text-align:left;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px;line-height:20px;}.t0c1{text-align:right;direction:rtl}.t0c2{background-color:rgba(212,255,212,0.5);}.t0c3{background-color:rgba(212,212,255,0.5);}.t0c4{background-color:rgba(255,212,212,0.5);}.t0c5{border-left:1px solid #CCE5FF;font-size:11px;direction:ltr;text-align:left;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px;line-height:20px;}.secSep{width:1100px;background-color:rgba(0,170,220,1) !important;;font-size:14px !important;font-weight:bold !important;color:white !important;}.ch1,.ch2,.ch3,.ch4,.ch5,.ch6,.ch7,.ch8{background-color:#ffa5a5}div#main>div:nth-child(2n){width:1100px;background-color:#e2e2e2;}.sr{background-color:#aaaaff !important;}</style><div class="other" id="header" style="white-space:nowrap;position:fixed;top:50px;height:18px;right:3px;left:283px;overflow-y:hidden;overflow-x:hidden;background-color:#eeeeee;z-index:9"><div style="width:50px;text-align:right" class="t0head" onclick="mw.ChSortF(\'l18\')">نماد</div><div style="width:150px;text-align:right" class="t0head" onclick="mw.ChSortF(\'l30\')">نام</div><div style="width:40px" class="t0head" onclick="mw.ChSortF(\'tno\')">تعداد</div><div style="width:60px" class="t0head"onclick="mw.ChSortF(\'tvol\')">حجم</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'tval\')">ارزش</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'py\')">دیروز</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'pf\')">اولین</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'pl\')">آخرین</div><div style="width:35px" class="t0head" onclick="mw.ChSortF(\'plc\')">تغییر</div><div style="width:35px" class="t0head" onclick="mw.ChSortF(\'plp\')">درصد</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'pc\')">پایانی</div><div style="width:35px" class="t0head" onclick="mw.ChSortF(\'pcc\')">تغییر</div><div style="width:35px" class="t0head" onclick="mw.ChSortF(\'pcp\')">درصد</div><div style="width:70px" class="t0head" onclick="mw.ChSortF(\'pmin\')">کمترین</div><div style="width:70px" class="t0head" onclick="mw.ChSortF(\'pmax\')">بیشترین</div><div style="width:45px" class="t0head" onclick="mw.ChSortF(\'eps\')">EPS</div><div style="width:45px" class="t0head" onclick="mw.ChSortF(\'pe\')">P/E</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'pd1\')">خرید</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'po1\')">فروش</div><div style="width:15px" class="t0head" ></div></div><div class="other" id="main" style="{s};top:68px;left:283px;right:3px;overflow-y:scroll;" onscroll="document.getElementById(\'header\').scrollLeft=document.getElementById(\'main\').scrollLeft"></div><div id="footer"></div>',
    rowStyle: "cursor:pointer;height:20px;white-space:nowrap;line-height:20px;",
    row: '<div style="width:50px" class="t0c t0c1"><a class=\'inst\' href=\'loader.aspx?ParTree=151311&i={i}\' target=\'{i}\'>{l18}</a></div><div style="width:150px" class="t0c t0c1"><a class=\'inst\' href=\'loader.aspx?ParTree=151311&i={i}\' target=\'{i}\'>{l30}</a></div><div style="width:40px" class="t0c5 ch{_tno}">{tno}</div><div style="width:60px" class="t0c5 ch{_tvol}">{tvol}</div><div style="width:60px" class="t0c5 ch{_tval}">{tval}</div><div style="width:60px" class="t0c5">{py}</div><div style="width:60px" class="t0c ch{_pf}">{pf}</div><div style="width:60px" class="t0c t0c2 ch{_pl}">{pl}</div><div style="width:35px" class="t0c t0c2 ch{_plc}">{plc}</div><div style="width:35px" class="t0c t0c2 ch{_plp}">{plp}</div><div style="width:60px" class="t0c ch{_pc}">{pc}</div><div style="width:35px" class="t0c ch{_pcc}">{pcc}</div><div style="width:35px" class="t0c ch{_pcp}">{pcp}</div><div style="width:70px" class="t0c5 ch{_pmin}">{pmin}</div><div style="width:70px" class="t0c5 ch{_pmax}">{pmax}</div><div style="width:45px" class="t0c5 ch{_eps}">{eps}</div><div style="width:45px" class="t0c ch{_pe}">{pe}</div><div style="width:60px" class="t0c t0c3 ch{_pd1}">{pd1}</div><div style="width:60px" class="t0c t0c4 ch{_po1}">{po1}</div>',
    excel: {
        header: "<tr><td>نماد</td><td>نام</td><td>تعداد</td><td>حجم</td><td>ارزش</td><td>دیروز</td><td>اولین</td><td>آخرین</td><td>تغییر</td><td>درصد</td><td>پایانی</td><td>تغییر</td><td>درصد</td><td>کمترین</td><td>بیشترین</td><td>EPS</td><td>P/E</td><td>خرید</td><td>فروش</td></tr>",
        row: "<tr><td>{l18}</td><td>{l30}</td><td>{tno}</td><td>{tvol}</td><td>{tval}</td><td>{py}</td><td>{pf}</td><td>{pl}</td><td>{plc}</td><td>{plp}</td><td>{pc}</td><td>{pcc}</td><td>{pcp}</td><td>{pmin}</td><td>{pmax}</td><td>{eps}</td><td>{pe}</td><td>{pd1}</td><td>{po1}</td></tr>"
    }
}, {
    title: "جدول ساده + عرضه و تقاضای 1 سطری",
    all: '<style>.t0head{cursor:pointer;border:0px solid #eeeeee;font-size:11px;direction:ltr;text-align:left;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c{border:0px solid #ffffff;font-size:11px;direction:ltr;text-align:left;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px;line-height:18px;height:20px;}.t0c1{text-align:right;direction:rtl}.t0c2{background-color:rgba(212,255,212,0.5);}.t0c3{background-color:rgba(212,212,255,0.5);}.t0c4{background-color:rgba(255,212,212,0.5);}.t0c5{border-left:1px solid #CCE5FF;font-size:11px;direction:ltr;text-align:left;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px;line-height:18px;height:20px;}.secSep{background-color:rgba(0,170,220,1) !important;;font-size:14px !important;;font-weight:bold !important;;color:white !important;}.ch1,.ch2,.ch3,.ch4,.ch5,.ch6,.ch7,.ch8{background-color:#ffa5a5}div#main>div:nth-child(3n){background-color:#e2e2e2;}div#main>div:nth-child(3n+1){background-color:#f2f2f2;}.sr{background-color:#aaaaff !important;}</style><div class="other" id="header0" style="white-space:nowrap;position:fixed;top:50px;height:18px;right:3px;left:283px;overflow-y:hidden;overflow-x:hidden;background-color:#eeeeee;z-index:9"><div style="width:160px;text-align:right" class="t0head" onclick="mw.ChSortF(\'po1\')">نام</div><div style="width:40px" class="t0head" onclick="mw.ChSortF(\'tno\')">تعداد</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'tvol\')">حجم</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'tval\')">ارزش</div><div style="width:85px" class="t0head" onclick="mw.ChSortF(\'plp\')">آخرین معامله</div><div style="width:85px" class="t0head" onclick="mw.ChSortF(\'pcp\')">قیمت پایانی</div><div style="width:55px" class="t0head" onclick="mw.ChSortF(\'pd1\')">خرید</div><div style="width:55px" class="t0head" onclick="mw.ChSortF(\'po1\')">فروش</div><div style="width:2px" class="t0head"></div><div style="width:160px" class="t0head" onclick="mw.ChSortF(\'po1\')">نام</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'tno\')">تعداد</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'tvol\')">حجم</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'tval\')">ارزش</div><div style="width:85px" class="t0head" onclick="mw.ChSortF(\'plp\')">آخرین معامله</div><div style="width:85px" class="t0head" onclick="mw.ChSortF(\'pcp\')">قیمت پایانی</div><div style="width:55px" class="t0head" onclick="mw.ChSortF(\'pd1\')">خرید</div><div style="width:55px" class="t0head" onclick="mw.ChSortF(\'po1\')">فروش</div><div style="width:2px" class="t0head"></div><div style="width:160px" class="t0head" onclick="mw.ChSortF(\'po1\')">نام</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'tno\')">تعداد</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'tvol\')">حجم</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'tval\')">ارزش</div><div style="width:85px" class="t0head" onclick="mw.ChSortF(\'plp\')">آخرین معامله</div><div style="width:85px" class="t0head" onclick="mw.ChSortF(\'pcp\')">قیمت پایانی</div><div style="width:55px" class="t0head" onclick="mw.ChSortF(\'pd1\')">خرید</div><div style="width:55px" class="t0head" onclick="mw.ChSortF(\'po1\')">فروش</div><div style="width:15px" class="t0head" ></div></div><div class="other" id="main" style="{s};top:68px;left:283px;right:3px;overflow-y:scroll;" onscroll="document.getElementById(\'header0\').scrollLeft=document.getElementById(\'main\').scrollLeft;"></div><div id="footer"></div>',
    rowStyle: "display:inline-block;cursor:pointer;height:20px;white-space:nowrap;padding:0px;margin:0px;line-height:18px",
    row: '<div style="width:160px" class="t0c t0c1 ch{_l30}"><a class=\'inst\' href=\'loader.aspx?ParTree=151311&i={i}\' target=\'{i}\'>{l30} ({l18})</a></div><div style="width:40px" class="t0c ch{_tno}">{tno}</div><div style="width:60px" class="t0c ch{_tvol}">{tvol}</div><div style="width:60px" class="t0c ch{_tval}">{tval}</div><div style="width:50px" class="t0c t0c2 ch{_pl}">{pl}</div><div style="width:35px" class="t0c t0c2 ch{_plp}">{plp}%</div><div style="width:50px" class="t0c ch{_pc}">{pc}</div><div style="width:35px" class="t0c ch{_pcp}">{pcp}%</div><div style="width:55px" class="t0c t0c3 ch{_pd1}">{pd1}</div><div style="width:55px" class="t0c t0c4 ch{_po1}">{po1}</div>',
    excel: {
        header: "<tr><td>نام</td><td>تعداد</td><td>حجم</td><td>ارزش</td><td>آخرین</td><td>پایانی</td><td>خرید</td><td>فروش</td></tr>",
        row: "<tr><td>{l30}</td><td>{tno}</td><td>{tvol}</td><td>{tval}</td><td>{pl}</td><td>{pc}</td><td>{pd1}</td><td>{po1}</td></tr>"
    }
}, {
    title: "جدول + عرضه و تقاضای 1 سطری",
    all: '<style>.t0head{cursor:pointer;border:0px solid #eeeeee;font-size:11px;direction:ltr;text-align:left;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c{border:0px solid #ffffff;font-size:11px;direction:ltr;text-align:left;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px;line-height:17px;}.t0c1{text-align:right;direction:rtl}.t0c2{background-color:rgba(212,255,212,0.5);}.t0c3{background-color:rgba(212,212,255,0.5);}.t0c4{background-color:rgba(255,212,212,0.5);}.t0c5{border-left:1px solid #CCE5FF;font-size:11px;direction:ltr;text-align:left;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px;line-height:17px;}.secSep{width:1292px;background-color:rgba(10,170,220,1) !important;;font-size:14px !important;;font-weight:bold !important;;color:white !important;}.ch1,.ch2,.ch3,.ch4,.ch5,.ch6,.ch7,.ch8{background-color:#ffa5a5}div#main>div:nth-child(2n){width:1292px;background-color:#e2e2e2;}.sr{background-color:#aaaaff !important;}</style><div class="other" id="header0" style="white-space:nowrap;position:fixed;top:50px;height:18px;right:3px;left:283px;overflow-y:hidden;overflow-x:hidden;background-color:#eeeeee;z-index:9"><div style="width:50px;text-align:right" class="t0head" onclick="mw.ChSortF(\'l18\')">نماد</div><div style="width:140px;text-align:right" class="t0head" onclick="mw.ChSortF(\'l30\')">نام</div><div style="width:40px" class="t0head" onclick="mw.ChSortF(\'tno\')">تعداد</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'tvol\')">حجم</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'tval\')">ارزش</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'py\')">دیروز</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'pf\')">اولین</div><div style="width:140px" class="t0head">آخرین معامله</div><div style="width:140px" class="t0head">قیمت پایانی</div><div style="width:70px" class="t0head" onclick="mw.ChSortF(\'pmin\')">کمترین</div><div style="width:70px" class="t0head" onclick="mw.ChSortF(\'pmax\')">بیشترین</div><div style="width:45px" class="t0head" onclick="mw.ChSortF(\'eps\')">EPS</div><div style="width:45px" class="t0head" onclick="mw.ChSortF(\'pe\')">P/E</div><div style="width:150px" class="t0head">خرید</div><div style="width:150px" class="t0head">فروش</div><div style="width:15px" class="t0head"></div></div><div class="other" id="header1" style="white-space:nowrap;position:fixed;top:68px;height:18px;right:3px;left:283px;overflow-y:hidden;overflow-x:hidden;background-color:#eeeeee;z-index:9"><div style="width:470px" class="t0head"></div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'pl\')">مقدار</div><div style="width:45px" class="t0head"  onclick="mw.ChSortF(\'plc\')">تغییر</div><div style="width:45px" class="t0head" onclick="mw.ChSortF(\'plp\')">درصد</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'pc\')">مقدار</div><div style="width:45px" class="t0head" onclick="mw.ChSortF(\'pcc\')">تغییر</div><div style="width:45px" class="t0head" onclick="mw.ChSortF(\'pcp\')">درصد</div><div style="width:230px" class="t0head"></div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'zd1\')">تعداد</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'qd1\')">حجم</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'pd1\')">قیمت</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'po1\')">قیمت</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'qo1\')">حجم</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'zo1\')">تعداد</div><div style="width:15px" class="t0head"></div></div><div class="other" id="main" style="{s};top:86px;left:283px;right:3px;overflow-y:scroll;" onscroll="document.getElementById(\'header0\').scrollLeft=document.getElementById(\'main\').scrollLeft;document.getElementById(\'header1\').scrollLeft=document.getElementById(\'main\').scrollLeft"></div><div id="footer"></div>',
    rowStyle: "cursor:pointer;white-space:nowrap;height:17px;line-height:17px",
    row: '<div style="width:50px" class="t0c t0c1"><a class=\'inst\' href=\'loader.aspx?ParTree=151311&i={i}\' target=\'{i}\'>{l18}</a></div><div style="width:140px" class="t0c t0c1"><a class=\'inst\' href=\'loader.aspx?ParTree=151311&i={i}\' target=\'{i}\'>{l30}</a></div><div style="width:40px" class="t0c5 ch{_tno}">{tno}</div><div style="width:60px" class="t0c5 ch{_tvol}">{tvol}</div><div style="width:60px" class="t0c5 ch{_tval}">{tval}</div><div style="width:60px" class="t0c5">{py}</div><div style="width:60px" class="t0c5 ch{_pf}">{pf}</div><div style="width:50px" class="t0c t0c2 ch{_pl}">{pl}</div><div style="width:45px" class="t0c t0c2 ch{_plc}">{plc}</div><div style="width:45px" class="t0c t0c2 ch{_plp}">{plp}</div><div style="width:50px" class="t0c ch{_pc}">{pc}</div><div style="width:45px" class="t0c ch{_pcc}">{pcc}</div><div style="width:45px" class="t0c ch{_pcp}">{pcp}</div><div style="width:70px" class="t0c5 ch{_pmin}">{pmin}</div><div style="width:70px" class="t0c5 ch{_pmax}">{pmax}</div><div style="width:45px" class="t0c5 ch{_eps}">{eps}</div><div style="width:45px" class="t0c ch{_pe}">{pe}</div><div style="width:50px" class="t0c5 t0c3 ch{_zd1}">{zd1}</div><div style="width:50px" class="t0c5 t0c3 ch{_qd1}">{qd1}</div><div style="width:50px" class="t0c t0c3 ch{_pd1}">{pd1}</div><div style="width:50px" class="t0c5 t0c4 ch{_po1}">{po1}</div><div style="width:50px" class="t0c5 t0c4 ch{_qo1}">{qo1}</div><div style="width:50px" class="t0c t0c4 ch{_zo1}">{zo1}</div>',
    excel: {
        header: "<tr><td>نماد</td><td>نام</td><td>تعداد</td><td>حجم</td><td>ارزش</td><td>دیروز</td><td>اولین</td><td colspan='3'>آخرین</td><td colspan='3'>پایانی</td><td>کمترین</td><td>بیشترین</td><td>EPS</td><td>P/E</td><td colspan='3'>خرید</td><td colspan='3'>فروش</td></tr><tr><td colspan='7'><td>مقدار</td><td>تغییر</td><td>درصد</td><td>مقدار</td><td>تغییر</td><td>درصد</td><td colspan='4'></td><td>تعداد</td><td>حجم</td><td>قیمت</td><td>قیمت</td><td>حجم</td><td>تعداد</td></tr>",
        row: "<tr><td>{l18}</td><td>{l30}</td><td>{tno}</td><td>{tvol}</td><td>{tval}</td><td>{py}</td><td>{pf}</td><td>{pl}</td><td>{plc}</td><td>{plp}</td><td>{pc}</td><td>{pcc}</td><td>{pcp}</td><td>{pmin}</td><td>{pmax}</td><td>{eps}</td><td>{pe}</td><td>{zd1}</td><td>{qd1}</td><td>{pd1}</td><td>{po1}</td><td>{qo1}</td><td>{zo1}</td></tr>"
    }
}, {
    title: "جدول + عرضه و تقاضای 3 سطری",
    all: '<style>.t0head{cursor:pointer;border:0px solid #eeeeee;font-size:11px;direction:ltr;text-align:left;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c{border:0px solid #ffffff;font-size:11px;direction:ltr;text-align:left;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px;line-height:20px}.t0c1{text-align:right;direction:rtl}.t0c2{background-color:rgba(212,255,212,0.5)}.t0c3{background-color:rgba(212,212,255,0.5)}.t0c4{background-color:rgba(255,212,212,0.5)}.secSep{background-color:rgba(0,170,220,1) !important;;font-size:14px !important;;font-weight:bold !important;;color:white !important;}.ch1,.ch2,.ch3,.ch4,.ch5,.ch6,.ch7,.ch8{background-color:#fff5f5}div#main>div:nth-child(2n){background-color:#e2e2e2;}.sr{background-color:#aaaaff !important;}</style><div class="other" id="header0" style="white-space:nowrap;position:fixed;top:50px;height:18px;right:3px;left:283px;overflow-y:hidden;overflow-x:hidden;background-color:#eeeeee;z-index:9"><div style="width:50px;text-align:right" class="t0head" onclick="mw.ChSortF(\'l18\')">نماد</div><div style="width:140px;text-align:right" class="t0head" onclick="mw.ChSortF(\'l30\')">نام</div><div style="width:40px" class="t0head" onclick="mw.ChSortF(\'tno\')">تعداد</div><div style="width:70px" class="t0head" onclick="mw.ChSortF(\'tvol\')">حجم</div><div style="width:70px" class="t0head" onclick="mw.ChSortF(\'tval\')">ارزش</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'py\')">دیروز</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'pf\')">اولین</div><div style="width:120px" class="t0head">آخرین معامله</div><div style="width:120px" class="t0head">قیمت پایانی</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'pmin\')">کمترین</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'pmax\')">بیشترین</div><div style="width:35px" class="t0head" onclick="mw.ChSortF(\'eps\')">EPS</div><div style="width:35px" class="t0head" onclick="mw.ChSortF(\'pe\')">P/E</div><div style="width:140px" class="t0head">خرید</div><div style="width:140px" class="t0head">فروش</div></div><div class="other" id="header1" style="white-space:nowrap;position:fixed;top:68px;height:18px;right:3px;left:283px;overflow-y:hidden;overflow-x:hidden;background-color:#eeeeee;z-index:9"><div style="width:470px" class="t0head "></div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'pl\')">مقدار</div><div style="width:35px" class="t0head"  onclick="mw.ChSortF(\'plc\')">تغییر</div><div style="width:35px" class="t0head" onclick="mw.ChSortF(\'plp\')">درصد</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'pc\')">مقدار</div><div style="width:35px" class="t0head" onclick="mw.ChSortF(\'pcc\')">تغییر</div><div style="width:35px" class="t0head" onclick="mw.ChSortF(\'pcp\')">درصد</div><div style="width:170px" class="t0head"></div><div style="width:40px" class="t0head" onclick="mw.ChSortF(\'zd1\')">تعداد</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'qd1\')">حجم</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'pd1\')">قیمت</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'po1\')">قیمت</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'qo1\')">حجم</div><div style="width:40px" class="t0head" onclick="mw.ChSortF(\'zo1\')">تعداد</div></div><div class="other" id="main" style="{s};top:86px;left:283px;right:3px;overflow-y:scroll;" onscroll="document.getElementById(\'header0\').scrollLeft=document.getElementById(\'main\').scrollLeft;document.getElementById(\'header1\').scrollLeft=document.getElementById(\'main\').scrollLeft"></div><div id="footer"></div>',
    rowStyle: "",
    row: '<div style="cursor:pointer;height:20px;white-space:nowrap;padding:0px;margin:0px"><div style="width:50px" class="t0c t0c1"><a class=\'inst\' href=\'loader.aspx?ParTree=151311&i={i}\' target=\'{i}\'>{l18}</a></div><div style="width:140px" class="t0c t0c1"><a class=\'inst\' href=\'loader.aspx?ParTree=151311&i={i}\' target=\'{i}\'>{l30}</a></div><div style="width:40px" class="t0c ch{_tno}">{tno}</div><div style="width:70px" class="t0c ch{_tvol}">{tvol}</div><div style="width:70px" class="t0c ch{_tval}">{tval}</div><div style="width:50px" class="t0c">{py}</div><div style="width:50px" class="t0c ch{_pf}">{pf}</div><div style="width:50px" class="t0c t0c2 ch{_pl}">{pl}</div><div style="width:35px" class="t0c t0c2 ch{_plc}">{plc}</div><div style="width:35px" class="t0c t0c2 ch{_plp}">{plp}</div><div style="width:50px" class="t0c ch{_pc}">{pc}</div><div style="width:35px" class="t0c ch{_pcc}">{pcc}</div><div style="width:35px" class="t0c ch{_pcp}">{pcp}</div><div style="width:50px" class="t0c ch{_pmin}">{pmin}</div><div style="width:50px" class="t0c ch{_pmax}">{pmax}</div><div style="width:35px" class="t0c ch{_eps}">{eps}</div><div style="width:35px" class="t0c ch{_pe}">{pe}</div><div style="width:40px" class="t0c t0c3 ch{_zd1}">{zd1}</div><div style="width:50px" class="t0c t0c3 ch{_qd1}">{qd1}</div><div style="width:50px" class="t0c t0c3 ch{_pd1}">{pd1}</div><div style="width:50px" class="t0c t0c4 ch{_po1}">{po1}</div><div style="width:50px" class="t0c t0c4 ch{_qo1}">{qo1}</div><div style="width:40px" class="t0c t0c4 ch{_zo1}">{zo1}</div></div><div ondblclick="ManageBaskets(\'{i}\')" style="cursor:pointer;height:20px;white-space:nowrap;padding:0px;margin:0px"><div style="width:880px" class="t0c"></div><div style="width:40px" class="t0c t0c3 ch{_zd2}">{zd2}</div><div style="width:50px" class="t0c t0c3 ch{_qd2}">{qd2}</div><div style="width:50px" class="t0c t0c3 ch{_pd2}">{pd2}</div><div style="width:50px" class="t0c t0c4 ch{_po2}">{po2}</div><div style="width:50px" class="t0c t0c4 ch{_qo2}">{qo2}</div><div style="width:40px" class="t0c t0c4 ch{_zo2}">{zo2}</div></div><div ondblclick="ManageBaskets(\'{i}\')" style="cursor:pointer;height:20px;white-space:nowrap;padding:0px;margin:0px"><div style="width:880px" class="t0c"></div><div style="width:40px" class="t0c t0c3 ch{_zd3}">{zd3}</div><div style="width:50px" class="t0c t0c3 ch{_qd3}">{qd3}</div><div style="width:50px" class="t0c t0c3 ch{_pd3}">{pd3}</div><div style="width:50px" class="t0c t0c4 ch{_po3}">{po3}</div><div style="width:50px" class="t0c t0c4 ch{_qo3}">{qo3}</div><div style="width:40px" class="t0c t0c4 ch{_zo3}">{zo3}</div></div><div style=\'height:1px;background-color:black\'></div>',
    excel: {
        header: "<tr><td>نماد</td><td>نام</td><td>تعداد</td><td>حجم</td><td>ارزش</td><td>دیروز</td><td>اولین</td><td colspan='3'>آخرین</td><td colspan='3'>پایانی</td><td>کمترین</td><td>بیشترین</td><td>EPS</td><td>P/E</td><td colspan='3'>خرید</td><td colspan='3'>فروش</td></tr><tr><td colspan='7'><td>مقدار</td><td>تغییر</td><td>درصد</td><td>مقدار</td><td>تغییر</td><td>درصد</td><td colspan='4'></td><td>تعداد</td><td>حجم</td><td>قیمت</td><td>قیمت</td><td>حجم</td><td>تعداد</td></tr>",
        row: "<tr><td>{l18}</td><td>{l30}</td><td>{tno}</td><td>{tvol}</td><td>{tval}</td><td>{py}</td><td>{pf}</td><td>{pl}</td><td>{plc}</td><td>{plp}</td><td>{pc}</td><td>{pcc}</td><td>{pcp}</td><td>{pmin}</td><td>{pmax}</td><td>{eps}</td><td>{pe}</td><td>{zd1}</td><td>{qd1}</td><td>{pd1}</td><td>{po1}</td><td>{qo1}</td><td>{zo1}</td></tr><tr><td colspan='17'></td><td>{zd2}</td><td>{qd2}</td><td>{pd2}</td><td>{po2}</td><td>{qo2}</td><td>{zo2}</td></tr><tr><td colspan='17'></td><td>{zd3}</td><td>{qd3}</td><td>{pd3}</td><td>{po3}</td><td>{qo3}</td><td>{zo3}</td></tr>"
    }
}, {
    title: "جدول + فیلد های کاربر",
    all: '<style>.t0head{cursor:pointer;border:0px solid #eeeeee;font-size:11px;direction:ltr;text-align:left;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c{border:0px solid #ffffff;font-size:11px;direction:ltr;text-align:left;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px;line-height:17px;}.t0c1{text-align:right;direction:rtl}.t0c2{background-color:rgba(212,255,212,0.5);}.t0c3{background-color:rgba(212,212,255,0.5);}.t0c4{background-color:rgba(255,212,212,0.5);}.t0c5{border-left:1px solid #CCE5FF;font-size:11px;direction:ltr;text-align:left;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px;line-height:17px;}.secSep{width:1475px;background-color:rgba(0,170,220,1) !important;;font-size:14px !important;;font-weight:bold !important;;color:white !important;}.ch1,.ch2,.ch3,.ch4,.ch5,.ch6,.ch7,.ch8{background-color:#ffa5a5}div#main>div:nth-child(2n){width:1475px;background-color:#e2e2e2;}.sr{background-color:#aaaaff !important;}</style><div class="other" id="header0" style="white-space:nowrap;position:fixed;top:50px;height:18px;right:3px;left:283px;overflow-y:hidden;overflow-x:hidden;background-color:#eeeeee;z-index:9"><div style="width:50px;text-align:right" class="t0head" onclick="mw.ChSortF(\'l18\')">نماد</div><div style="width:140px;text-align:right" class="t0head" onclick="mw.ChSortF(\'l30\')">نام</div><div style="width:40px" class="t0head" onclick="mw.ChSortF(\'tno\')">تعداد</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'tvol\')">حجم</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'tval\')">ارزش</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'py\')">دیروز</div><div style="width:60px" class="t0head" onclick="mw.ChSortF(\'pf\')">اولین</div><div style="width:140px" class="t0head">آخرین معامله</div><div style="width:140px" class="t0head">قیمت پایانی</div><div style="width:70px" class="t0head" onclick="mw.ChSortF(\'pmin\')">کمترین</div><div style="width:70px" class="t0head" onclick="mw.ChSortF(\'pmax\')">بیشترین</div><div style="width:45px" class="t0head" onclick="mw.ChSortF(\'eps\')">EPS</div><div style="width:45px" class="t0head" onclick="mw.ChSortF(\'pe\')">P/E</div><div style="width:150px" class="t0head">خرید</div><div style="width:150px" class="t0head">فروش</div><div style="width:60px" class="t0head">C0</div><div style="width:60px" class="t0head">C1</div><div style="width:60px" class="t0head">C2</div><div style="width:15px" class="t0head"></div></div><div class="other" id="header1" style="white-space:nowrap;position:fixed;top:68px;height:18px;right:3px;left:283px;overflow-y:hidden;overflow-x:hidden;background-color:#eeeeee;z-index:9"><div style="width:470px" class="t0head"></div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'pl\')">مقدار</div><div style="width:45px" class="t0head"  onclick="mw.ChSortF(\'plc\')">تغییر</div><div style="width:45px" class="t0head" onclick="mw.ChSortF(\'plp\')">درصد</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'pc\')">مقدار</div><div style="width:45px" class="t0head" onclick="mw.ChSortF(\'pcc\')">تغییر</div><div style="width:45px" class="t0head" onclick="mw.ChSortF(\'pcp\')">درصد</div><div style="width:230px" class="t0head"></div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'zd1\')">تعداد</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'qd1\')">حجم</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'pd1\')">قیمت</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'po1\')">قیمت</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'qo1\')">حجم</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'zo1\')">تعداد</div><div style="width:180px" class="t0head"></div><div style="width:15px" class="t0head"></div></div><div class="other" id="main" style="{s};top:86px;left:283px;right:3px;overflow-y:scroll;" onscroll="document.getElementById(\'header0\').scrollLeft=document.getElementById(\'main\').scrollLeft;document.getElementById(\'header1\').scrollLeft=document.getElementById(\'main\').scrollLeft"></div><div id="footer"></div>',
    rowStyle: "cursor:pointer;white-space:nowrap;height:17px;line-height:17px",
    row: '<div style="width:50px" class="t0c t0c1"><a class=\'inst\' href=\'loader.aspx?ParTree=151311&i={i}\' target=\'{i}\'>{l18}</a></div><div style="width:140px" class="t0c t0c1"><a class=\'inst\' href=\'loader.aspx?ParTree=151311&i={i}\' target=\'{i}\'>{l30}</a></div><div style="width:40px" class="t0c5 ch{_tno}">{tno}</div><div style="width:60px" class="t0c5 ch{_tvol}">{tvol}</div><div style="width:60px" class="t0c5 ch{_tval}">{tval}</div><div style="width:60px" class="t0c5">{py}</div><div style="width:60px" class="t0c5 ch{_pf}">{pf}</div><div style="width:50px" class="t0c t0c2 ch{_pl}">{pl}</div><div style="width:45px" class="t0c t0c2 ch{_plc}">{plc}</div><div style="width:45px" class="t0c t0c2 ch{_plp}">{plp}</div><div style="width:50px" class="t0c ch{_pc}">{pc}</div><div style="width:45px" class="t0c ch{_pcc}">{pcc}</div><div style="width:45px" class="t0c ch{_pcp}">{pcp}</div><div style="width:70px" class="t0c5 ch{_pmin}">{pmin}</div><div style="width:70px" class="t0c5 ch{_pmax}">{pmax}</div><div style="width:45px" class="t0c5 ch{_eps}">{eps}</div><div style="width:45px" class="t0c ch{_pe}">{pe}</div><div style="width:50px" class="t0c5 t0c3 ch{_zd1}">{zd1}</div><div style="width:50px" class="t0c5 t0c3 ch{_qd1}">{qd1}</div><div style="width:50px" class="t0c t0c3 ch{_pd1}">{pd1}</div><div style="width:50px" class="t0c5 t0c4 ch{_po1}">{po1}</div><div style="width:50px" class="t0c5 t0c4 ch{_qo1}">{qo1}</div><div style="width:50px" class="t0c t0c4 ch{_zo1}">{zo1}</div><div style="width:60px" class="t0c">{cfield0}</div><div style="width:60px" class="t0c">{cfield1}</div><div style="width:60px" class="t0c">{cfield2}</div>',
    excel: {
        header: "<tr><td>نماد</td><td>نام</td><td>تعداد</td><td>حجم</td><td>ارزش</td><td>دیروز</td><td>اولین</td><td colspan='3'>آخرین</td><td colspan='3'>پایانی</td><td>کمترین</td><td>بیشترین</td><td>EPS</td><td>P/E</td><td colspan='3'>خرید</td><td colspan='3'>فروش</td></tr><tr><td colspan='7'><td>مقدار</td><td>تغییر</td><td>درصد</td><td>مقدار</td><td>تغییر</td><td>درصد</td><td colspan='4'></td><td>تعداد</td><td>حجم</td><td>قیمت</td><td>قیمت</td><td>حجم</td><td>تعداد</td><td>C0</td><td>C1</td><td>C2</td></tr>",
        row: "<tr><td>{l18}</td><td>{l30}</td><td>{tno}</td><td>{tvol}</td><td>{tval}</td><td>{py}</td><td>{pf}</td><td>{pl}</td><td>{plc}</td><td>{plp}</td><td>{pc}</td><td>{pcc}</td><td>{pcp}</td><td>{pmin}</td><td>{pmax}</td><td>{eps}</td><td>{pe}</td><td>{zd1}</td><td>{qd1}</td><td>{pd1}</td><td>{po1}</td><td>{qo1}</td><td>{zo1}</td><td>{cfield0}</td><td>{cfield1}</td><td>{cfield2}</td></tr>"
    }
}, {
    title: "کارتی 1",
    all: '<style>.t0c{font-size:11px;direction:rtl;text-align:right;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c1{font-weight:bold;display:inline-block;}.t0c2{border:0px solid #ffffff;font-size:11px;direction:ltr;text-align:center;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c3{border:0px solid #ffffff;font-size:11px;direction:rtl;text-align:right;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c4{background-color:rgba(212,212,255,0.5);}.t0c5{background-color:rgba(255,212,212,0.5);}.secSep{background-color:rgba(0,170,220,1) !important;;font-size:14px !important;;font-weight:bold !important;;color:white !important;}.ch1,.ch2,.ch3,.ch4,.ch5,.ch6,.ch7,.ch8{background-color:#ffa5a5}.sr{background-color:#aaaaff !important;}</style><div class="other" id="main" style="{s};top:50px;left:283px;right:3px;overflow-y:scroll"></div>',
    rowStyle: "border:1px solid black;display:inline-block;width:180px;height:20px;padding:2px;margin:2px;vertical-align:top",
    row: "<div class=\"t0c3 ch{_l30}\"><a class='inst' href='loader.aspx?ParTree=151311&i={i}' target='{i}'>{l18}</a></div><div style='width:110px' class=\"t0c2 ch{_pl}\">{pl}&nbsp;{plc}&nbsp;{plp}%</div>"
}, {
    title: "کارتی 2",
    all: '<style>.t0c{font-size:11px;direction:rtl;text-align:right;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c1{font-weight:bold}.t0c2{border:0px solid #ffffff;font-size:11px;direction:ltr;text-align:center;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c3{border:0px solid #ffffff;font-size:11px;direction:rtl;text-align:right;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c4{background-color:rgba(212,212,255,0.5);}.t0c5{background-color:rgba(255,212,212,0.5);}.secSep{background-color:rgba(0,170,220,1) !important;;font-size:14px !important;;font-weight:bold !important;;color:white !important;}.ch1,.ch2,.ch3,.ch4,.ch5,.ch6,.ch7,.ch8{background-color:#ffa5a5}.sr{background-color:#aaaaff !important;}</style><div class="other" id="main" style="{s};top:50px;left:283px;right:3px;overflow-y:scroll"></div>',
    rowStyle: "border:1px solid black;display:inline-block;width:290px;height:45px;padding:2px;margin:2px;vertical-align:top",
    row: "<div class=\"t0c1 ch{_l30}\"><a class='inst' href='loader.aspx?ParTree=151311&i={i}' target='{i}'>{l18}&nbsp-&nbsp;{l30}</a></div><div style='width:35px' class=\"t0c3 ch{_pl}\">آخرین</div><div style='width:100px' class=\"t0c2 ch{_pl}\">{pl}&nbsp;{plc}&nbsp;{plp}%</div><div style='width:35px' class=\"t0c3 ch{_pc}\">پایانی</div><div style='width:100px' class=\"t0c2 ch{_pc}\">{pc}&nbsp;{pcc}&nbsp;{pcp}%</div><br/><div style='width:35px' class=\"t0c3 ch{_tno}\">تعداد</div><div style='width:60px' class=\"t0c2 ch{_tno}\">{tno}</div><div style='width:35px' class=\"t0c3 ch{_tvol}\">حجم</div><div style='width:60px' class=\"t0c2 ch{_tvol}\">{tvol}</div><div style='width:35px' class=\"t0c3 ch{_tval}\">ارزش</div><div style='width:60px' class=\"t0c2 ch{_tval}\">{tval}</div>"
}, {
    title: "کارتی + عرضه و تقاضا 1 سطری بدون عنوان",
    all: '<style>.t0c{font-size:11px;direction:rtl;text-align:right;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c1{font-weight:bold}.t0c2{border:0px solid #ffffff;font-size:11px;direction:ltr;text-align:center;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c3{border:0px solid #ffffff;font-size:11px;direction:rtl;text-align:right;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c4{background-color:rgba(212,212,255,0.5);}.t0c5{background-color:rgba(255,212,212,0.5);}.secSep{background-color:rgba(0,170,220,1) !important;;font-size:14px !important;;font-weight:bold !important;;color:white !important;}.ch1,.ch2,.ch3,.ch4,.ch5,.ch6,.ch7,.ch8{background-color:#ffa5a5}.sr{background-color:#aaaaff !important;}</style><div class="other" id="main" style="{s};top:50px;left:283px;right:3px;overflow-y:scroll"></div>',
    rowStyle: "background-repeat:no-repeat;background-position:left top;background-size:50px 17px;background-image:url('tsev2/chart/img/Inst.aspx?i={i}');border:1px solid black;display:inline-block;width:275px;height:60px;padding:2px;margin:2px;vertical-align:top",
    row: '<div class="t0c1 ch{_l30}"><a class=\'inst\' href=\'loader.aspx?ParTree=151311&i={i}\' target=\'{i}\'>{l18}&nbsp-&nbsp;{l30}</a></div><div><div style=\'width:35px\' class="t0c3">آخرین</div><div style=\'width:100px\' class="t0c2 ch{_pl}">{pl}&nbsp;{plc}&nbsp;{plp}%</div><div style=\'width:35px\' class="t0c3">پایانی</div><div style=\'width:100px\' class="t0c2 ch{_pc}">{pc}&nbsp;{pcc}&nbsp;{pcp}%</div><br/><div style=\'width:30px\' class="t0c3">تعداد</div><div style=\'width:60px\' class="t0c2 ch{_tno}">{tno}</div><div style=\'width:30px\' class="t0c3">حجم</div><div style=\'width:60px\' class="t0c2 ch{_tvol}">{tvol}</div><div style=\'width:30px\' class="t0c3">ارزش</div><div style=\'width:60px\' class="t0c2 ch{_tval}">{tval}</div></div><div style="cursor:pointer;height:17px;white-space:nowrap;padding:0px;margin:0px"><div style="width:35px" title="تعداد" class="t0c t0c4 ch{_zd1}">{zd1}</div><div style="width:50px" title="حجم" class="t0c t0c4 ch{_qd1}">{qd1}</div><div style="width:50px" title="قیمت" class="t0c t0c4 ch{_pd1}">{pd1}</div><div style="width:50px" title="قیمت" class="t0c t0c5 ch{_po1}">{po1}</div><div style="width:50px" title="حجم" class="t0c t0c5 ch{_qo1}">{qo1}</div><div style="width:35px" title="تعداد" class="t0c t0c5 ch{_zo1}">{zo1}</div></div></div>'
}, {
    title: "کارتی + عرضه و تقاضا 1 سطری",
    all: '<style>.t0c{font-size:11px;direction:rtl;text-align:right;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c1{font-weight:bold}.t0c2{border:0px solid #ffffff;font-size:11px;direction:ltr;text-align:center;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c3{border:0px solid #ffffff;font-size:11px;direction:rtl;text-align:right;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c4{background-color:rgba(212,212,255,0.5);}.t0c5{background-color:rgba(255,212,212,0.5);}.secSep{background-color:rgba(0,170,220,1) !important;;font-size:14px !important;;font-weight:bold !important;;color:white !important;}.ch1,.ch2,.ch3,.ch4,.ch5,.ch6,.ch7,.ch8{background-color:#ffa5a5}.sr{background-color:#aaaaff !important;}</style><div class="other" id="main" style="{s};top:50px;left:283px;right:3px;overflow-y:scroll"></div>',
    rowStyle: "background-repeat:no-repeat;background-position:left top;background-size:50px 17px;background-image:url('tsev2/chart/img/Inst.aspx?i={i}');border:1px solid black;display:inline-block;width:275px;height:80px;padding:2px;margin:2px;vertical-align:top",
    row: '<div class="t0c1 ch{_l30}"><a class=\'inst\' href=\'loader.aspx?ParTree=151311&i={i}\' target=\'{i}\'>{l18}&nbsp-&nbsp;{l30}</a></div><div><div style=\'width:35px\' class="t0c3">آخرین</div><div style=\'width:100px\' class="t0c2 ch{_pl}">{pl}&nbsp;{plc}&nbsp;{plp}%</div><div style=\'width:35px\' class="t0c3">پایانی</div><div style=\'width:100px\' class="t0c2 ch{_pc}">{pc}&nbsp;{pcc}&nbsp;{pcp}%</div><br/><div style=\'width:30px\' class="t0c3">تعداد</div><div style=\'width:60px\' class="t0c2 ch{_tno}">{tno}</div><div style=\'width:30px\' class="t0c3">حجم</div><div style=\'width:60px\' class="t0c2 ch{_tvol}">{tvol}</div><div style=\'width:30px\' class="t0c3">ارزش</div><div style=\'width:60px\' class="t0c2 ch{_tval}">{tval}</div></div><div style=\'margin:2px\'><div style="cursor:pointer;height:17px;white-space:nowrap;padding:0px;margin:0px"><div style="width:35px" class="t0c t0c4">تعداد</div><div style="width:50px" class="t0c t0c4">حجم</div><div style="width:50px" class="t0c t0c4">قیمت</div><div style="width:50px" class="t0c t0c5">قیمت</div><div style="width:50px" class="t0c t0c5">حجم</div><div style="width:35px" class="t0c t0c5">تعداد</div></div><div style="cursor:pointer;height:17px;white-space:nowrap;padding:0px;margin:0px"><div style="width:35px" class="t0c t0c4 ch{_zd1}">{zd1}</div><div style="width:50px" class="t0c t0c4 ch{_qd1}">{qd1}</div><div style="width:50px" class="t0c t0c4 ch{_pd1}">{pd1}</div><div style="width:50px" class="t0c t0c5 ch{_po1}">{po1}</div><div style="width:50px" class="t0c t0c5 ch{_qo1}">{qo1}</div><div style="width:35px" class="t0c t0c5 ch{_zo1}">{zo1}</div></div></div>'
}, {
    title: "کارتی + عرضه و تقاضا 3 سطری",
    all: '<style>.t0c{font-size:11px;direction:rtl;text-align:right;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c1{font-weight:bold}.t0c2{border:0px solid #ffffff;font-size:11px;direction:ltr;text-align:center;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c3{border:0px solid #ffffff;font-size:11px;direction:rtl;text-align:right;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c4{background-color:rgba(212,212,255,0.5);}.t0c5{background-color:rgba(255,212,212,0.5);}.secSep{background-color:rgba(0,170,220,1) !important;;font-size:14px !important;;font-weight:bold !important;;color:white !important;}.ch1,.ch2,.ch3,.ch4,.ch5,.ch6,.ch7,.ch8{background-color:#ffa5a5}.sr{background-color:#aaaaff !important;}</style><div class="other" id="main" style="{s};top:50px;left:283px;right:3px;overflow-y:scroll"></div>',
    rowStyle: "background-repeat:no-repeat;background-position:left top;background-size:50px 17px;background-image:url('tsev2/chart/img/Inst.aspx?i={i}');border:1px solid black;display:inline-block;width:275px;height:115px;padding:2px;margin:2px;vertical-align:top",
    row: '<div class="t0c1 ch{_l30}"><a class=\'inst\' href=\'loader.aspx?ParTree=151311&i={i}\' target=\'{i}\'>{l18}&nbsp-&nbsp;{l30}</a></div><div><div style=\'width:35px\' class="t0c3">آخرین</div><div style=\'width:100px\' class="t0c2 ch{_pl}">{pl}&nbsp;{plc}&nbsp;{plp}%</div><div style=\'width:35px\' class="t0c3">پایانی</div><div style=\'width:100px\' class="t0c2 ch{_pc}">{pc}&nbsp;{pcc}&nbsp;{pcp}%</div><br/><div style=\'width:30px\' class="t0c3">تعداد</div><div style=\'width:60px\' class="t0c2 ch{_tno}">{tno}</div><div style=\'width:30px\' class="t0c3">حجم</div><div style=\'width:60px\' class="t0c2 ch{_tvol}">{tvol}</div><div style=\'width:30px\' class="t0c3">ارزش</div><div style=\'width:60px\' class="t0c2 ch{_tval}">{tval}</div></div><div style=\'margin:2px\'><div style="cursor:pointer;height:17px;white-space:nowrap;padding:0px;margin:0px"><div style="width:35px" class="t0c t0c4">تعداد</div><div style="width:50px" class="t0c t0c4">حجم</div><div style="width:50px" class="t0c t0c4">قیمت</div><div style="width:50px" class="t0c t0c5">قیمت</div><div style="width:50px" class="t0c t0c5">حجم</div><div style="width:35px" class="t0c t0c5">تعداد</div></div><div style="cursor:pointer;height:17px;white-space:nowrap;padding:0px;margin:0px"><div style="width:35px" class="t0c t0c4 ch{_zd1}">{zd1}</div><div style="width:50px" class="t0c t0c4 ch{_qd1}">{qd1}</div><div style="width:50px" class="t0c t0c4 ch{_pd1}">{pd1}</div><div style="width:50px" class="t0c t0c5 ch{_po1}">{po1}</div><div style="width:50px" class="t0c t0c5 ch{_qo1}">{qo1}</div><div style="width:35px" class="t0c t0c5 ch{_zo1}">{zo1}</div></div><div style="cursor:pointer;height:17px;white-space:nowrap;padding:0px;margin:0px"><div style="width:35px" class="t0c t0c4 ch{_zd2}">{zd2}</div><div style="width:50px" class="t0c t0c4 ch{_qd2}">{qd2}</div><div style="width:50px" class="t0c t0c4 ch{_pd2}">{pd2}</div><div style="width:50px" class="t0c t0c5 ch{_po2}">{po2}</div><div style="width:50px" class="t0c t0c5 ch{_qo2}">{qo2}</div><div style="width:35px" class="t0c t0c5 ch{_zo2}">{zo2}</div></div><div style="cursor:pointer;height:17px;white-space:nowrap;padding:0px;margin:0px"><div style="width:35px" class="t0c t0c4 ch{_zd3}">{zd3}</div><div style="width:50px" class="t0c t0c4 ch{_qd3}">{qd3}</div><div style="width:50px" class="t0c t0c4 ch{_pd3}">{pd3}</div><div style="width:50px" class="t0c t0c5 ch{_po3}">{po3}</div><div style="width:50px" class="t0c t0c5 ch{_qo3}">{qo3}</div><div style="width:35px" class="t0c t0c5 ch{_zo3}">{zo3}</div></div></div>'
}, {
    title: "قیمت، عرضه و تقاضا",
    all: '<style>.t0head{cursor:pointer;border:0px solid #eeeeee;font-size:11px;direction:ltr;text-align:left;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c{border:0px solid #ffffff;font-size:11px;direction:ltr;text-align:left;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px;height:20px}.t0c1{text-align:right;direction:rtl}.t0c2{background-color:rgba(212,255,212,0.5);}.t0c3{background-color:rgba(212,212,255,0.5);}.t0c4{background-color:rgba(255,212,212,0.5);}.secSep{background-color:rgba(0,170,220,1) !important;;font-size:14px !important;;font-weight:bold !important;;color:white !important;}.ch1,.ch2,.ch3,.ch4,.ch5,.ch6,.ch7,.ch8{background-color:#ffa5a5}div#main>div:nth-child(2n){background-color:#e2e2e2;}.sr{background-color:#aaaaff !important;}</style><div class="other" id="header0" style="white-space:nowrap;position:fixed;top:50px;height:18px;right:3px;left:283px;overflow-y:hidden;overflow-x:hidden;background-color:#eeeeee;z-index:9"><div style="width:150px;text-align:right" class="t0head" onclick="mw.ChSortF(\'po1\')">نام</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'plp\')">آخرین</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'pd1\')">خرید</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'po1\')">فروش</div><div style="width:150px;text-align:right" class="t0head" onclick="mw.ChSortF(\'po1\')">نام</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'plp\')">آخرین</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'pd1\')">خرید</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'po1\')">فروش</div><div style="width:150px;text-align:right" class="t0head" onclick="mw.ChSortF(\'po1\')">نام</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'plp\')">آخرین</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'pd1\')">خرید</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'po1\')">فروش</div><div style="width:150px;text-align:right" class="t0head" onclick="mw.ChSortF(\'po1\')">نام</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'plp\')">آخرین</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'pd1\')">خرید</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'po1\')">فروش</div><div style="width:150px;text-align:right" class="t0head" onclick="mw.ChSortF(\'po1\')">نام</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'plp\')">آخرین</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'pd1\')">خرید</div><div style="width:50px" class="t0head" onclick="mw.ChSortF(\'po1\')">فروش</div></div><div class="other" id="main" style="{s};top:68px;left:283px;right:3px;overflow-y:scroll;" onscroll="document.getElementById(\'header0\').scrollLeft=document.getElementById(\'main\').scrollLeft;"></div><div id="footer"></div>',
    rowStyle: "display:inline-block;cursor:pointer;height:20px;white-space:nowrap;padding:0px 0px 0px 0px;margin:0px 0px 0px 0px;line-height:20px",
    row: '<div style="width:150px" class="t0c t0c1 ch{_l30}"><a class=\'inst\' href=\'loader.aspx?ParTree=151311&i={i}\' target=\'{i}\'>{l30} ({l18})</a></div><div style="width:50px" class="t0c t0c2 ch{_pl}">{pl}</div><div style="width:50px" class="t0c t0c3 ch{_pd1}">{pd1}</div><div style="width:50px" class="t0c t0c4 ch{_po1}">{po1}</div>'
}, {
    title: "شخصی",
    all: "",
    rowStyle: "",
    row: "",
    excel: {
        header: "",
        row: ""
    }
}];
;function MarketWatchPlus() {
    var MarketWatchPlus = {
        persianOrder: {
            "آ": "0",
            "ا": "1",
            "ا": "1",
            "ب": "2",
            "پ": "3",
            "ت": "4",
            "ث": "5",
            "ج": "6",
            "چ": "7",
            "ح": "8",
            "خ": "9",
            "د": "a",
            "ذ": "b",
            "ر": "c",
            "ز": "d",
            "ژ": "e",
            "س": "f",
            "ش": "g",
            "ص": "h",
            "ض": "i",
            "ط": "j",
            "ظ": "k",
            "ع": "l",
            "غ": "m",
            "ف": "n",
            "ق": "o",
            "ك": "p",
            "ک": "p",
            "گ": "q",
            "گ": "q",
            "ل": "r",
            "م": "s",
            "ن": "t",
            "و": "u",
            "ه": "v",
            "ه": "v",
            "ی": "w"
        },
        field: {
            l18: "نماد",
            l30: "نام",
            tno: "تعداد",
            tvol: "حجم",
            tval: "ارزش",
            py: "قیمت دیروز",
            pf: "اولین قیمت",
            pmin: "کمترین قیمت",
            pmax: "بیشترین قیمت",
            pl: "آخرین قیمت",
            plc: "تغییر آخرین قیمت",
            plp: "درصد تغییر آخرین قیمت",
            pc: "آخرین قیمت",
            pcc: "تغییر قیمت پایانی",
            pcp: "درصد تغییر قیمت پایانی",
            eps: "EPS",
            pe: "P/E",
            pd1: "قیمت خرید",
            zd1: "تعداد خریدار",
            qd1: "حجم خرید",
            po1: "قیمت فروش",
            zo1: "تعداد فروشنده",
            qo1: "حجم فروش",
            visitcount: "تعداد بازدید - پربیننده",
            heven: "زمان آخرین معامله",
            mv: "تعداد سهام",
            cfield0: "cfield0",
            cfield1: "cfield1",
            cfield2: "cfield2"
        },
        SetPreviewDefault: function() {
            var MarketWatchPreview = localStorage.getItem("MarketWatchPreview");
            if (MarketWatchPreview == null) {
                var ismobile = navigator.userAgent.match(/(iPad)|(iPhone)|(iPod)|(android)|(webOS)/i);
                if (ismobile == null) {
                    MarketWatchPreview = "block"
                } else {
                    MarketWatchPreview = ""
                }
            }
            mw.ShowHidePreview(MarketWatchPreview)
        },
        ShowHidePreview: function(mode) {
            if (typeof mode == "undefined") {
                mode = $(document.getElementById("infop")).css("display");
                if (mode == "block") {
                    mode = ""
                } else {
                    mode = "block"
                }
            }
            localStorage.setItem("MarketWatchPreview", mode);
            if (mode != "block") {
                $("#infop").css("display", "none");
                $(".other").css("left", "3px")
            } else {
                $("#infop").css("display", "block");
                $(".other").css("left", "283px")
            }
        },
        ShowVol: function(vol, base) {
            if (mw.Settings.BigNumberSymbol == 1) {
                var iVal = parseInt(vol, 10);
                var sVal;
                if (iVal > 1000000000) {
                    sVal = addCommas(Math.round(iVal / 1000000) / 1000) + "B"
                } else {
                    if (iVal > 1000000) {
                        sVal = addCommas(Math.round(iVal / 1000) / 1000) + "M"
                    } else {
                        sVal = addCommas(iVal)
                    }
                }
                var stl = "";
                stl = iVal > parseInt(base) ? 'style="font-weight:bold"' : "";
                return "<span title='حجم: " + addCommas(vol) + " حجم مبنا: " + addCommas(base) + "' " + stl + ">" + sVal + "</span>"
            } else {
                var iVal = parseInt(vol, 10);
                var stl = "";
                stl = iVal > parseInt(base) ? 'style="font-weight:bold"' : "";
                return "<span title='حجم: " + addCommas(vol) + " حجم مبنا: " + addCommas(base) + "' " + stl + ">" + addCommas(vol) + "</span>"
            }
        },
        DefaultSettings: {
            UpdateSpeed: 1000,
            ColorChangeSpeed: 7000,
            ColorChangeEnable: 1,
            ViewMode: 1,
            Market: 0,
            BasketNo: -1,
            FilterNo: -1,
            SectorNo: "",
            sortField: "tno",
            sortDirection: -1,
            ActiveTemplate: 2,
            Baskets: [],
            Filters: [],
            GroupBySector: 1,
            LightBackground: 1,
            BigNumberSymbol: 1,
            ShowHousingFacilities: 1,
            ShowSaham: 1,
            ShowPayeFarabourse: 0,
            ShowHaghTaghaddom: 1,
            ShowOraghMosharekat: 1,
            ShowEkhtiarForoush: 1,
            ShowAti: 1,
            ShowSandoogh: 1,
            ShowKala: 1,
            AutoScroll: 0,
            LoadClientType: 0,
            LoadInstStat: 0,
            LoadInstHistory: 0,
            CustomTemplate: {
                colNo: 10,
                fontSize: 12,
                rowHeight: 20,
                cols: [],
                all: "",
                rowStyle: "",
                row: ""
            }
        },
        UpdateCounter: 0,
        UpdateIgnore: 0,
        NotificationPermission: false,
        FirstTime: true,
        RoundNo: 1,
        AllRows: {},
        ClientType: {},
        InstStat: {},
        InstHistory: {},
        Settings: {},
        BasketInsts: "",
        FilterCode: "",
        userFullName: undefined,
        refid: 0,
        heven: 0,
        preOpen: true,
        RenderPreviewOne: function(row) {
            if (row == 0) {
                return ""
            }
            var data = mw.AllRows[row];
            if (data.preview.length == 0) {
                var mv = AdvRound(data.pc * parseFloat(data.z) / 1000000000, 2);
                data.preview = "<span style='font-size:14px;font-weight:bold'>" + data.l18 + " - " + data.l30 + "</span><table border='0' style='width:100%'><tr><td>آخرین معامله</td><td>" + addCommas(data.pl) + "</td><td>" + colorNum(data.plc) + "</td><td>" + colorNum(data.plp) + "%</td></tr><tr><td>قیمت پایانی</td><td>" + addCommas(data.pc) + "</td><td>" + colorNum(data.pcc) + "</td><td>" + colorNum(data.pcp) + "%</td></tr><tr><td>قیمت دیروز</td><td>" + addCommas(data.py) + "</td><td>اولین</td><td>" + addCommas(data.pf) + "</td></tr><tr><td>بازه روز</td><td colspan='3'>" + addCommas(data.pmax) + "&nbsp;" + addCommas(data.pmin) + "</td></tr><tr><td>قیمت مجاز</td><td colspan='3'>" + addCommas(data.tmax) + "&nbsp;" + addCommas(data.tmin) + "</td></tr><tr><td colspan='4' style='height:1px;background-color:#999999;margin:0px;padding:0px'></td></tr><tr><td>تعداد</td><td>" + addCommas(data.tno) + "</td><td>ارزش</td><td>" + bigNumber(data.tval) + "</td></tr><tr><td>حجم</td><td>" + mw.ShowVol(data.tvol, data.bvol) + "</td><td>مبنا</td><td>" + bigNumber(data.bvol) + "</td></tr><tr><td colspan='2'>ارزش بازار به میلیارد</td><td colspan='2'>" + addCommas(mv) + "</td><tr><td colspan='4' style='height:1px;background-color:#999999;margin:0px;padding:0px'></td></tr><tr><td>EPS</td><td>" + data.eps + "</td><td>P/E</td><td>" + data.pe + '</td></tr></table><style>.info-r{background-color:#ffdddd}.info-b{background-color:#ddddff}</style><table border=\'0\' style="width:100%"><tr><td class="info-b">تعداد</td><td class="info-b">حجم</td><td class="info-b">قیمت</td><td class="info-r">قیمت</td><td class="info-r">حجم</td><td class="info-r">تعداد</td></tr><tr><td class="info-b">' + data.zd1 + '</td><td class="info-b">' + addCommas(data.qd1) + '</td><td class="info-b">' + data.pd1 + '</td><td class="info-r">' + data.po1 + '</td><td class="info-r">' + addCommas(data.qo1) + '</td><td class="info-r">' + data.zo1 + '</td></tr><tr><td class="info-b">' + data.zd2 + '</td><td class="info-b">' + addCommas(data.qd2) + '</td><td class="info-b">' + data.pd2 + '</td><td class="info-r">' + data.po2 + '</td><td class="info-r">' + addCommas(data.qo2) + '</td><td class="info-r">' + data.zo2 + '</td></tr><tr><td class="info-b">' + data.zd3 + '</td><td class="info-b">' + addCommas(data.qd3) + '</td><td class="info-b">' + data.pd3 + '</td><td class="info-r">' + data.po3 + '</td><td class="info-r">' + addCommas(data.qo3) + '</td><td class="info-r">' + data.zo3 + "</td></tr></table><hr/>";
                if (typeof mw.ClientType[row] != "undefined") {
                    var ct = mw.ClientType[row];
                    data.preview += '<table style="width:100%"><tr><td></td><td>خرید</td><td>فروش</td><tr><td>حقیقی (حجم)</td><td class="ltr">' + bigNumber(ct.Buy_I_Volume) + '</td><td class="ltr" id="e3">' + bigNumber(ct.Sell_I_Volume) + '</td><tr><td>حقوقی (حجم)</td><td class="ltr">' + bigNumber(ct.Buy_N_Volume) + '</td><td class="ltr" id="e3">' + bigNumber(ct.Sell_N_Volume) + '</td><tr><td>تعداد</td><td class="ltr">' + (ct.Buy_CountI + ct.Buy_CountN) + '</td><td class="ltr" id="e3">' + (ct.Sell_CountI + ct.Sell_CountN) + '</td><tr><td>حقیقی (تعداد)</td><td class="ltr">' + ct.Buy_CountI + '</td><td class="ltr" id="e3">' + ct.Sell_CountN + '</td><tr><td>حقوقی (تعداد)</td><td class="ltr">' + ct.Buy_CountN + '</td><td class="ltr" id="e3">' + ct.Sell_CountN + "</td></table></div>"
                }
            }
            return data.preview
        },
        RenderPreview: function() {
            if (mw.SelectedRow == 0) {
                $(document.getElementById("infos")).html("<div style='color:red'>امکان ساخت ستون جدید بر اساس فرمول شما فراهم شد. به راهنما مراجعه کنید.</div><hr/><div>اطلاعات سایقه تا 3 ماه قبل (60 روز معاملاتی) فراهم شد</div><div>امکان استفاده از تابع، حلقه، شرط و ... در فیلتر اضافه شد. به راهنما مراجعه کنید.</div><div>امکان استفاده از سابقه قیمت ها در ساخت فیلتر اضافه شد</div><div>امکان استفاده از اطلاعات حقیقی و حقوقی و آمارهای کلیدی در ساخت فیلتر اضافه شد</div>")
            } else {
                $(document.getElementById("infos")).html(mw.RenderPreviewOne(mw.SelectedRow) + mw.RenderPreviewOne(mw.PreSelectedRow))
            }
        },
        SelectRow: function(row, InsCode) {
            if (mw.SelectedRow == InsCode) {
                return
            }
            if (document.getElementById(mw.SelectedRow) == null) {
                mw.SelectedRow = 0
            }
            if (mw.SelectedRow != 0) {
                document.getElementById(mw.SelectedRow).className = ""
            }
            row.className = "sr";
            mw.PreSelectedRow = mw.SelectedRow;
            mw.SelectedRow = InsCode;
            window.setTimeout("mw.RenderPreview()", 25)
        },
        ChSortF: function(field) {
            if (mw.Settings.sortField == field) {
                mw.ChangeSortDir(-mw.Settings.sortDirection);
                return
            }
            mw.Settings.sortField = field;
            mw.SaveParams();
            mw.SortData();
            mw.ShowSettings()
        },
        ChangeSortDir: function(dir) {
            mw.Settings.sortDirection = dir;
            mw.SaveParams();
            mw.SortData();
            mw.ShowSettings()
        },
        changeTemplate: function(index) {
            mw.Settings.ActiveTemplate = index;
            $("#display").html(MWTemplates[mw.Settings.ActiveTemplate].all);
            for (var key in mw.AllRows) {
                if (mw.AllRows.hasOwnProperty(key)) {
                    mw.AllRows[key].render = ""
                }
            }
            mw.SaveParams();
            mw.RenderData()
        },
        SortData: function() {
            switch (mw.Settings.sortField) {
            case "l18":
            case "l30":
                var list = $(document.getElementById("main").childNodes).get();
                list.sort(function(a, b) {
                    var a1;
                    var b1;
                    if (mw.Settings.sortDirection == 1) {
                        a1 = "000";
                        b1 = "000"
                    } else {
                        a1 = "ییی";
                        b1 = "ییی"
                    }
                    var as = "";
                    var bs = "";
                    if (mw.Settings.GroupBySector == 1) {
                        if (a.id[0] == "S") {
                            as = a.id.substring(1)
                        } else {
                            as = mw.AllRows[a.id]["cs"]
                        }
                        if (b.id[0] == "S") {
                            bs = b.id.substring(1)
                        } else {
                            bs = mw.AllRows[b.id]["cs"]
                        }
                    }
                    if (a.id[0] != "S") {
                        a1 = mw.AllRows[a.id][mw.Settings.sortField];
                        if (typeof mw.persianOrder[a1[0]] != "string") {
                            a1 = a1.substring(1)
                        }
                        a1 = mw.persianOrder[a1[0]] + a1
                    }
                    if (b.id[0] != "S") {
                        b1 = mw.AllRows[b.id][mw.Settings.sortField];
                        if (typeof mw.persianOrder[b1[0]] != "string") {
                            b1 = b1.substring(1)
                        }
                        b1 = mw.persianOrder[b1[0]] + b1
                    }
                    return as == bs ? (a1 == b1 ? 0 : (a1 > b1 ? mw.Settings.sortDirection : -mw.Settings.sortDirection)) : (as > bs ? -1 : 1)
                });
                var ParentNode = document.getElementById("main");
                for (var i = 0; i < list.length; i++) {
                    if (ParentNode.childNodes[i] != list[i]) {
                        ParentNode.appendChild(list[i])
                    }
                }
                break;
            case "mv":
                var list = $(document.getElementById("main").childNodes).get();
                list.sort(function(a, b) {
                    var a1;
                    var b1;
                    if (mw.Settings.sortDirection == 1) {
                        a1 = -999999999999999;
                        b1 = -999999999999999
                    } else {
                        a1 = 999999999999999;
                        b1 = 999999999999999
                    }
                    var as = "";
                    var bs = "";
                    if (mw.Settings.GroupBySector == 1) {
                        if (a.id[0] == "S") {
                            as = a.id.substring(1)
                        } else {
                            as = mw.AllRows[a.id]["cs"]
                        }
                        if (b.id[0] == "S") {
                            bs = b.id.substring(1)
                        } else {
                            bs = mw.AllRows[b.id]["cs"]
                        }
                    }
                    if (a.id[0] != "S") {
                        a1 = parseFloat(mw.AllRows[a.id]["pc"]) * parseFloat(mw.AllRows[a.id]["z"])
                    }
                    if (b.id[0] != "S") {
                        b1 = parseFloat(mw.AllRows[b.id]["pc"]) * parseFloat(mw.AllRows[b.id]["z"])
                    }
                    return as == bs ? (a1 == b1 ? 0 : (a1 > b1 ? mw.Settings.sortDirection : -mw.Settings.sortDirection)) : (as > bs ? -1 : 1)
                });
                var ParentNode = document.getElementById("main");
                for (var i = 0; i < list.length; i++) {
                    if (ParentNode.childNodes[i] != list[i]) {
                        ParentNode.appendChild(list[i])
                    }
                }
                break;
            default:
                var list = $(document.getElementById("main").childNodes).get();
                list.sort(function(a, b) {
                    var a1;
                    var b1;
                    if (mw.Settings.sortDirection == 1) {
                        a1 = -999999999999999;
                        b1 = -999999999999999
                    } else {
                        a1 = 999999999999999;
                        b1 = 999999999999999
                    }
                    var as = "";
                    var bs = "";
                    if (mw.Settings.GroupBySector == 1) {
                        if (a.id[0] == "S") {
                            as = a.id.substring(1)
                        } else {
                            as = mw.AllRows[a.id]["cs"]
                        }
                        if (b.id[0] == "S") {
                            bs = b.id.substring(1)
                        } else {
                            bs = mw.AllRows[b.id]["cs"]
                        }
                    }
                    if (a.id[0] != "S") {
                        a1 = parseFloat(mw.AllRows[a.id][mw.Settings.sortField])
                    }
                    if (b.id[0] != "S") {
                        b1 = parseFloat(mw.AllRows[b.id][mw.Settings.sortField])
                    }
                    return as == bs ? (a1 == b1 ? 0 : (a1 > b1 ? mw.Settings.sortDirection : -mw.Settings.sortDirection)) : (as > bs ? -1 : 1)
                });
                var ParentNode = document.getElementById("main");
                for (var i = 0; i < list.length; i++) {
                    if (ParentNode.childNodes[i] != list[i]) {
                        ParentNode.appendChild(list[i])
                    }
                }
                break
            }
        },
        NumberOfInstruments: function(BasketCode) {
            var list = mw.Settings.Baskets[BasketCode].Instruments;
            if (list.length == 0) {
                return 0
            } else {
                return list.split(",").length
            }
        },
        SaveParams: function() {
            setData("MarketWatchSettings", JSON.stringify(mw.Settings))
        },
        ShowSettings: function() {
            var html;
            html = "<div style='display:inline-block;vertical-align:bottom;margin-top:6px;margin-right:9px'><a class='TopIcon MwIcon' href='/Loader.aspx?ParTree=15' id='home' desc='خانه,دسترسي سريع به صفحه اول سايت' onmouseover='ShowTooltip(this)' onmouseout='HideTooltip()' aria-label='خانه' role='img'></a><a class='TopIcon MwIcon' href='javascript:ShowSearchWindow()' id='search' desc='جستجو, جستجوی نمادها' onmouseover='ShowTooltip(this)' onmouseout='HideTooltip()' aria-label='جستجو' role='img'></a><a class='TopIcon MwIcon MwSetting' id='id1' href='#' onclick='mw.ShowAllSettings()' onmouseover='ShowTooltip(this)' onmouseout='HideTooltip()' desc='تنظیم ها, سرعت بروز رسانی - انتخاب بازار - انتخاب سبد - انتخاب گروه ' aria-label='تنظیمات دیده بان' role='img'></a><a class='TopIcon MwIcon MwSort' href='#' onclick='mw.ShowSortWindow()' onmouseover='ShowTooltip(this)' onmouseout='HideTooltip()' desc='مرتب سازی, انتخاب ترتیب نمایش اطلاعات' aria-label='مرتب سازی' role='img'></a><a class='TopIcon MwIcon MwTemplate' href='#' onclick='mw.ShowTemplateWindow()' onmouseover='ShowTooltip(this)' onmouseout='HideTooltip()' desc='قالب نمایش, انتخاب نحوه نمایش اطلاعات' aria-label='قالب نمایش' role='img'></a><a class='TopIcon MwIcon MwPreview' href='#' onclick='mw.ShowHidePreview()' onmouseover='ShowTooltip(this)' onmouseout='HideTooltip()' desc='مشاهده سریع, نمایش / عدم نمایش مشاهده سریع. با این امکان با انتخاب هر نماد اطلاعات آن در سمت چپ نمایش داده می شود' aria-label='مشاهده سریع' role='img'></a><a class='TopIcon MwIcon MwQuery' href='#' onclick='mw.QueryWindow()' onmouseover='ShowTooltip(this)' onmouseout='HideTooltip()' desc='فیلتر,مدیریت و ساخت فیلتر' aria-label='فیلتر نویسی' role='img'></a><a class='TopIcon MwIcon MwExcel' href='#' onclick='mw.ExportWindow()' onmouseover='ShowTooltip(this)' onmouseout='HideTooltip()' desc='خروجی, ساخت فایل از اطلاعات معاملات' aria-label='تهیه خروجی' role='img' ></a><a class=\"TopIcon\" href=\"javascript:ShowHelpWindow('151715',true)\" id=\"book\" desc=\"راهنما,آموزش امکانات دیده بان بازار\" onmouseover=\"ShowTooltip(this)\" onmouseout=\"HideTooltip()\" aria-label=\"راهنما\" role=\"img\" ></a></div><div style='width:330px;display:inline-block;padding:0px;margin;0px;height:38px;vertical-align:top;'>&nbsp;<div class='MwText' style='width:130px;height:30px'>ترتیب:" + mw.field[mw.Settings.sortField] + "&nbsp;(" + (mw.Settings.sortDirection == 1 ? "صعودی" : "نزولی") + ")</div>";
            var filter = "";
            if (mw.Settings.FilterNo != -1 && mw.Settings.FilterNo < mw.Settings.Filters.length) {
                filter = "<br/>" + mw.Settings.Filters[mw.Settings.FilterNo].FilterName
            }
            switch (mw.Settings.ViewMode) {
            case 0:
                html += "&nbsp;<div class='MwText' style='width:160px;height:30px'>نمایش همه نمادها";
                break;
            case 1:
                html += "&nbsp;<div class='MwText' style='width:160px;height:30px'>نمایش نمادهای معامله شده";
                break;
            case 2:
                html += "&nbsp;<div class='MwText' style='width:160px;height:30px'>نمایش سبد:" + mw.Settings.Baskets[mw.Settings.BasketNo].BasketName;
                break;
            case 3:
                html += "&nbsp;<div class='MwText' style='width:160px;height:30px'>نمایش گروه:" + mw.SectorName(mw.Settings.SectorNo);
                break
            }
            html += filter + "</div>";
            $("#SettingsDesc").html(html)
        },
        ExportWindow: function() {
            var html = "<div style='text-align:right'><div>خروجی اکسل از اطلاعات لحظه ای آخرین روز معاملاتی (با فرمت عددی)<br/>لینک: https://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d=0<div onclick='mw.ExportClick(\"lastexcel\")' style='float:left' class='awesome tra' role='button' aria-label='خروجی اکسل از اطلاعات لحظه ای آخرین روز معاملاتی با فرمت عددی' >تهیه خروجی</div></div><br/><hr/><div>خروجی اکسل از اطلاعات لحظه ای آخرین روز معاملاتی (بدون فرمت عددی)<br/>لینک: https://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d=0&format=0<div onclick='mw.ExportClick(\"lastexcelwf\")' style='float:left' class='awesome tra' role='button' aria-label='خروجی اکسل از اطلاعات لحظه ای آخرین روز معاملاتی با فرمت عددی' >تهیه خروجی</div><br/></div><br/><hr/><div>خروجی HTML از دیده بان بازار شما<div onclick='mw.ExportClick(\"yourmw\")' style='float:left' class='awesome tra' role='button' aria-label='خروجی HTML از دیده بان بازار شما' >تهیه خروجی</div></div><br/><hr/><div>خروجی اکسل از دیده بان بازار شما<div onclick='mw.ExportClick(\"yourmwexcel\")' style='float:left' class='awesome tra' role='button' aria-label='خروجی اکسل از دیده بان بازار شما' >تهیه خروجی</div></div><br/><hr/><div>خروجی اکسل از اطلاعات روزهای معاملاتی قبل<input id='exceldate' class='awesome tra' placeholder='تاریخ' aria-label='تاریخ' title='تاریخ' style='cursor:text'><div onclick='mw.ExportClick(\"dateexcel\")' style='float:left' class='awesome tra' role='button' aria-label='خروجی اکسل از اطلاعات روزهای معاملاتی قبل' >تهیه خروجی</div></div><br/><hr/></div>";
            var WinNo = ShowModalStaticPro("تهیه خروجی", html, 480, 320)
        },
        ExportClick: function(type) {
            switch (type) {
            case "lastexcel":
                window.location.href = "https://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d=0";
                break;
            case "lastexcelwf":
                window.location.href = "https://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d=0&format=0";
                break;
            case "yourmw":
                var html = "<html><head><meta charset='utf-8'></head><body style='direction:rtl;font-family:tahoma'>" + $("#display").html() + "</body></html>";
                html = html.replace(/left: 283px;/g, "").replace(/left:283px;/g, "");
                html = html.replace(/top: 50px;/g, "top: 0px;").replace(/top:50px;/g, "top: 0px;");
                html = html.replace(/top: 68px;/g, "top: 18px;").replace(/top:68px;/g, "top: 18px;");
                html = html.replace(/top: 86px;/g, "top: 36px;").replace(/top:86px;/g, "top: 36px;");
                html = html.replace(/loader.aspx/g, "http://www.tsetmc.com/loader.aspx");
                html = html.replace(/onclick=/g, "clk1=");
                html = html.replace(/ondblclick=/g, "clk2=");
                var blob = new Blob([html],{
                    type: "text/html;charset=utf-8"
                });
                saveAs(blob, "MarketWatch.htm");
                break;
            case "yourmwexcel":
                if (typeof MWTemplates[mw.Settings.ActiveTemplate].excel == "undefined") {
                    window.location.href = "https://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d=0";
                    break
                }
                var html = "<html><head><meta charset='utf-8'></head><body style='direction:rtl;font-family:tahoma'><table>" + MWTemplates[mw.Settings.ActiveTemplate].excel.header + mw.RenderExcelData() + "</table></body></html>";
                var blob = new Blob([html],{
                    type: "text/html;charset=utf-8"
                });
                saveAs(blob, "MarketWatch.xls");
                break;
            case "dateexcel":
                var d = $("#exceldate").val();
                d = $("<div />").text(d).html();
                if (!validDate(d)) {
                    return
                }
                window.location.href = "https://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d=" + d;
                break
            }
        },
        RenderOneExcel: function(row) {
            var rowHTML = MWTemplates[mw.Settings.ActiveTemplate].excel.row;
            rowHTML = rowHTML.replace(/{i}/g, row.inscode);
            rowHTML = rowHTML.replace("{l18}", row.l18);
            rowHTML = rowHTML.replace("{l30}", row.l30);
            rowHTML = rowHTML.replace("{heven}", row.heven);
            rowHTML = rowHTML.replace("{pf}", addCommas(row.pf));
            rowHTML = rowHTML.replace("{pc}", addCommas(row.pc));
            rowHTML = rowHTML.replace("{pcc}", colorNum(row.pcc));
            rowHTML = rowHTML.replace("{pcp}", colorNum(row.pcp));
            rowHTML = rowHTML.replace("{pl}", addCommas(row.pl));
            rowHTML = rowHTML.replace("{plc}", colorNum(row.plc));
            rowHTML = rowHTML.replace("{plp}", colorNum(row.plp));
            rowHTML = rowHTML.replace("{tno}", addCommas(row.tno));
            rowHTML = rowHTML.replace("{tvol}", mw.ShowVol(row.tvol, row.bvol));
            rowHTML = rowHTML.replace("{tval}", mw.Settings.BigNumberSymbol == 1 ? bigNumber(row.tval) : addCommas(row.tval));
            rowHTML = rowHTML.replace("{pmin}", addCommas(row.pmin));
            rowHTML = rowHTML.replace("{pmax}", addCommas(row.pmax));
            rowHTML = rowHTML.replace("{py}", addCommas(row.py));
            rowHTML = rowHTML.replace("{eps}", row.eps == "" ? "-" : row.eps);
            rowHTML = rowHTML.replace("{pe}", row.pe == "" ? "-" : row.pe);
            rowHTML = rowHTML.replace("{bvol}", addCommas(row.bvol));
            rowHTML = rowHTML.replace("{zo1}", addCommas(row.zo1));
            rowHTML = rowHTML.replace("{zd1}", addCommas(row.zd1));
            rowHTML = rowHTML.replace("{pd1}", addCommas(row.pd1));
            rowHTML = rowHTML.replace("{po1}", addCommas(row.po1));
            rowHTML = rowHTML.replace("{qd1}", mw.Settings.BigNumberSymbol == 1 ? bigNumber(row.qd1) : addCommas(row.qd1));
            rowHTML = rowHTML.replace("{qo1}", mw.Settings.BigNumberSymbol == 1 ? bigNumber(row.qo1) : addCommas(row.qo1));
            rowHTML = rowHTML.replace("{zo2}", addCommas(row.zo2));
            rowHTML = rowHTML.replace("{zd2}", addCommas(row.zd2));
            rowHTML = rowHTML.replace("{pd2}", addCommas(row.pd2));
            rowHTML = rowHTML.replace("{po2}", addCommas(row.po2));
            rowHTML = rowHTML.replace("{qd2}", mw.Settings.BigNumberSymbol == 1 ? bigNumber(row.qd2) : addCommas(row.qd2));
            rowHTML = rowHTML.replace("{qo2}", mw.Settings.BigNumberSymbol == 1 ? bigNumber(row.qo2) : addCommas(row.qo2));
            rowHTML = rowHTML.replace("{zo3}", addCommas(row.zo3));
            rowHTML = rowHTML.replace("{zd3}", addCommas(row.zd3));
            rowHTML = rowHTML.replace("{pd3}", addCommas(row.pd3));
            rowHTML = rowHTML.replace("{po3}", addCommas(row.po3));
            rowHTML = rowHTML.replace("{qd3}", mw.Settings.BigNumberSymbol == 1 ? bigNumber(row.qd3) : addCommas(row.qd3));
            rowHTML = rowHTML.replace("{qo3}", mw.Settings.BigNumberSymbol == 1 ? bigNumber(row.qo3) : addCommas(row.qo3));
            rowHTML = rowHTML.replace("{cfield0}", row.cfield0);
            rowHTML = rowHTML.replace("{cfield1}", row.cfield1);
            rowHTML = rowHTML.replace("{cfield2}", row.cfield2);
            return rowHTML
        },
        RenderExcelData: function() {
            var flow;
            var BodyHTML = [];
            var RenderNo = 0;
            var yval = "";
            var html = "";
            for (var key in mw.AllRows) {
                if (!mw.AllRows.hasOwnProperty(key)) {
                    continue
                }
                var row = mw.AllRows[key];
                if (mw.preOpen == false && mw.Settings.ViewMode == 1 && row.tno == "0") {
                    continue
                }
                if (mw.Settings.ViewMode == 2 && mw.BasketInsts.indexOf(row.inscode) == -1) {
                    continue
                }
                if (mw.Settings.ViewMode == 3 && mw.Settings.SectorNo != row.cs) {
                    continue
                }
                flow = row.flow;
                if (mw.Settings.Market == 1 && (flow != "1" && flow != "3")) {
                    continue
                }
                if (mw.Settings.Market == 2 && (flow == "1" || flow == "3")) {
                    continue
                }
                if (mw.Settings.ShowHousingFacilities == 0) {
                    if (row.l18.indexOf("تسه") == 0 || row.l18.indexOf("تملي") == 0) {
                        continue
                    }
                }
                yval = row.yval;
                if (mw.Settings.ShowSaham == 0 && (yval == "300" || yval == "303" || yval == "313") && row.l18.indexOf("تسه") != 0) {
                    continue
                }
                if (mw.Settings.ShowPayeFarabourse == 0 && (yval == "309")) {
                    continue
                }
                if (mw.Settings.ShowHaghTaghaddom == 0 && (yval == "400" || yval == "403" || yval == "404")) {
                    continue
                }
                if (mw.Settings.ShowOraghMosharekat == 0 && (yval == "306" || yval == "301" || yval == "706" || yval == "208")) {
                    continue
                }
                if (mw.Settings.ShowAti == 0 && (yval == "263")) {
                    continue
                }
                if (mw.Settings.ShowSandoogh == 0 && (yval == "305" || yval == "380")) {
                    continue
                }
                if (mw.Settings.ShowEkhtiarForoush == 0 && (yval == "600" || yval == "602" || yval == "605" || yval == "311" || yval == "312")) {
                    continue
                }
                if (mw.Settings.ShowKala == 0 && (yval == "308" || yval == "701")) {
                    continue
                }
                if (mw.FilterCode.length != 0) {
                    var FilterResult;
                    try {
                        if (typeof mw.ClientType[row.inscode] == "undefined") {
                            mw.ClientType[row.inscode] = {
                                Buy_CountI: 0,
                                Buy_CountN: 0,
                                Buy_I_Volume: 0,
                                Buy_N_Volume: 0,
                                Sell_CountI: 0,
                                Sell_CountN: 0,
                                Sell_I_Volume: 0,
                                Sell_N_Volume: 0
                            }
                        }
                        FilterResult = eval(mw.FilterCode)
                    } catch (e) {
                        FilterResult = false
                    }
                    if (!FilterResult) {
                        continue
                    }
                }
                html += mw.RenderOneExcel(row)
            }
            return html
        },
        QueryWindow: function() {
            if ($("#FilterIndex").length != 0) {
                return
            }
            var height = $(window).height() - 165;
            var WinNo = ShowModalStaticPro("فیلتر", "<div id='FilterIndex' style='direction:ltr;text-align:right;overflow-y:scroll;overflow-x:none;display:inline-block;width:200px;height:" + height + "px'></div><div id='FilterContent' style='text-align:right;overflow:hidden;padding:5px;display:inline-block;width:765zpx;height:" + height + "px'></div>", 1000);
            mw.QueryWindowFilterNames()
        },
        QueryWindowFilterNames: function() {
            var html = "";
            if (mw.Settings.FilterNo != -1) {
                html += "<div class='awesome red' style='display:inline-block;width:150px' onclick=\"mw.SelectFilter(-1);mw.ShowSettings();mw.SaveParams();mw.QueryWindowFilterNames()\">نمایش اطلاعات بدون فیلتر</div>"
            }
            for (var ipos = 0; ipos < mw.Settings.Filters.length; ipos++) {
                mw.Settings.FilterNo == ipos ? cls = "" : cls = "tra";
                html += "<div class='awesome " + cls + "' style='display:inline-block;width:150px' onclick=\"mw.SelectFilter(" + ipos + ');mw.ShowSettings();mw.SaveParams();mw.QueryWindowFilterNames()">' + mw.Settings.Filters[ipos].FilterName + "</div>"
            }
            html += "<br/><div class='awesome black' style='display:inline-block;width:150px' onclick=\"mw.QueryWindowNewFilter();mw.QueryWindowFilterNames()\">فیلتر جدید</div>";
            mw.NotificationPermission ? cls = "" : cls = "tra";
            html += "<br/><div class='awesome " + cls + "' style='display:inline-block;width:150px' onclick=\"if(typeof Notification!='undefined')Notification.requestPermission(function(perm) {if(perm=='granted'){mw.NotificationPermission=!mw.NotificationPermission;mw.QueryWindowFilterNames()}});\">برای نمایش هشدار در هنگام اضافه/حذف نماد کلیک کنید</div>";
            html += "</div>";
            $("#FilterIndex").html(html);
            mw.QueryWindowEditFilter()
        },
        QueryWindowEditFilter: function() {
            var html = "";
            if (mw.Settings.FilterNo != -1) {
                var height = $(window).height() - 250;
                html += "<div class='awesome blue' style='display:inline-block;width:100px' onclick=\"mw.QueryWindowSaveFilter()\">ثبت</div>";
                html += "<div class='awesome ' style='display:inline-block;width:100px' onclick=\"mw.QueryWindowCheckFilter()\">اعتبار سنجی</div>";
                html += "<div class='awesome tra' style='display:inline-block;width:50px' onclick=\"mw.QueryWindowEditFilter()\">تصحیح</div>";
                html += "<div class='awesome red' style='display:inline-block;width:50px' onclick=\"mw.QueryWindowConfirmDeleteFilter()\">حذف فیلتر</div>";
                html += "<div style='float:left' class='awesome' onclick='ShowHelpWindow(\"151715\",true)'>راهنمای ساخت فیلتر</div>";
                html += "<br/>";
                html += "<div>نام فیلتر</div><input id='InputFilterName' style='width:750px' value='" + mw.Settings.Filters[mw.Settings.FilterNo].FilterName + "'/><br/><div>شرط</div><textarea id='InputFilterCode' style='border:0px;overflow:scroll;font:12px tahoma;direction:ltr;width:750px;height:" + height + "px;'>" + mw.Settings.Filters[mw.Settings.FilterNo].FilterCode + "</textarea>"
            }
            $("#FilterContent").html(html);
            $("#InputFilterCode").keydown(function(e) {
                if (e.keyCode === 9) {
                    var start = this.selectionStart;
                    var end = this.selectionEnd;
                    var $this = $(this);
                    var value = $this.val();
                    $this.val(value.substring(0, start) + "    " + value.substring(end));
                    this.selectionStart = this.selectionEnd = start + 3;
                    e.preventDefault()
                }
            })
        },
        QueryWindowConfirmDeleteFilter: function() {
            ShowConfirm({
                FireFunction: function() {
                    mw.Settings.Filters.splice(mw.Settings.FilterNo, 1);
                    mw.SaveParams();
                    mw.Settings.FilterNo = -1;
                    mw.QueryWindowFilterNames()
                }
            })
        },
        QueryWindowCheckFilter: function() {
            var filterRaw = $("#InputFilterCode").val();
            var filter = mw.PrepareFilterCode(filterRaw);
            var CheckResult = "خطایی در کد مشاهده نشد";
            if (filterRaw.indexOf("[is") != -1 && mw.Settings.LoadInstStat == 0) {
                CheckResult = "آمارهای کلیدی را در بخش تنظیمات - اطلاعات نکمیلی فعال کنید تا در فیلتر قابل استفاده باشد."
            } else {
                if (filterRaw.indexOf("(ct)") != -1 && mw.Settings.LoadClientType == 0) {
                    CheckResult = "حقیقی و حقوقی را در بخش تنظیمات - اطلاعات نکمیلی فعال کنید تا در فیلتر قابل استفاده باشد."
                } else {
                    if (filterRaw.indexOf("[ih]") != -1 && mw.Settings.LoadInstHistory == 0) {
                        CheckResult = "تاریخچه قیمت ها را در بخش تنظیمات - اطلاعات نکمیلی فعال کنید تا در فیلتر قابل استفاده باشد."
                    } else {
                        for (var key in mw.AllRows) {
                            if (mw.AllRows.hasOwnProperty(key)) {
                                var row = mw.AllRows[key];
                                try {
                                    if (typeof mw.ClientType[row.inscode] == "undefined") {
                                        mw.ClientType[row.inscode] = {
                                            Buy_CountI: 0,
                                            Buy_CountN: 0,
                                            Buy_I_Volume: 0,
                                            Buy_N_Volume: 0,
                                            Sell_CountI: 0,
                                            Sell_CountN: 0,
                                            Sell_I_Volume: 0,
                                            Sell_N_Volume: 0
                                        }
                                    }
                                    var DummyFilterResult = eval(filter);
                                    break
                                } catch (e) {
                                    CheckResult = "خطای زیر در هنگام اجرا مشاهده شد:<br/><div style='direction:ltr'>" + e + "</div>";
                                    break
                                }
                            }
                        }
                    }
                }
            }
            var WinNo = ShowModalStaticPro("اعتبار سنجی", CheckResult, 320, 240)
        },
        QueryWindowSaveFilter: function() {
            var inputFilterName = $("#InputFilterName").val();
            inputFilterName = $("<div />").text(inputFilterName).html();
            mw.Settings.Filters[mw.Settings.FilterNo].FilterName = inputFilterName;
            mw.Settings.Filters[mw.Settings.FilterNo].FilterCode = $("#InputFilterCode").val();
            mw.SaveParams();
            mw.SelectFilter(mw.Settings.FilterNo);
            mw.ShowSettings();
            mw.QueryWindowFilterNames()
        },
        QueryWindowNewFilter: function() {
            mw.Settings.Filters.push({
                FilterCode: "",
                FilterName: "فیلتر شماره " + mw.Settings.Filters.length
            });
            mw.SaveParams()
        },
        SectorName: function(SectorCode) {
            for (var ipos = 0; ipos < Sectors.length; ipos++) {
                if (SectorCode == Sectors[ipos][0]) {
                    return Sectors[ipos][1]
                }
            }
            return ""
        },
        ListBasket: function() {
            $.ajax({
                url: MembersSite() + "/tsev2/data/Baskets.aspx",
                type: "POST",
                crossDomain: true,
                xhrFields: {
                    withCredentials: true
                },
                cache: false,
                data: {
                    t: "list",
                    dt: 0
                },
                dataType: "html",
                error: function() {},
                success: function(data) {
                    var html = "";
                    if (data == "login") {
                        html = "<a href='" + MembersSite() + "/userloginnew.aspx?http://www.tsetmc.com/loader.aspx?ParTree=15131F' target='_top'> برای استفاده از این امکان می بایست عضو شوید و با نام کاربری خود وارد سایت شوید. برای ثبت نام یا ورود به سیستم کلیک کنید</a>";
                        ShowModalStaticPro("فهرست تنظیم های ذخیره شده", html, 200, 100)
                    } else {
                        if (data.length > 0) {
                            var rows = data.split(";");
                            var cols;
                            for (var ipos = 0; ipos < rows.length; ipos++) {
                                cols = rows[ipos].split(",");
                                html += '<div style="width:175px;margin:3px" class="awesome tra" onclick="mw.LoadBasket(' + cols[0] + ')">' + cols[1] + "</div>"
                            }
                            ShowModalStaticPro("فهرست تنظیم ها - تاریخ ذخیره سازی", html, 220, 400)
                        }
                    }
                }
            })
        },
        LoadBasket: function(BasketIdn) {
            $.ajax({
                url: MembersSite() + "/tsev2/data/Baskets.aspx",
                type: "POST",
                cache: false,
                crossDomain: true,
                xhrFields: {
                    withCredentials: true
                },
                data: {
                    t: "load",
                    b: BasketIdn
                },
                dataType: "html",
                success: function(data) {
                    if (data == "login") {
                        var html = "<a style='text-decoration:underline' href='" + MembersSite() + "/userloginnew.aspx?http://www.tsetmc.com/loader.aspx?ParTree=15131F' target='_top'> برای استفاده از این امکان می بایست عضو شوید و با نام کاربری خود وارد سایت شوید. برای ثبت نام یا ورود به سیستم کلیک کنید</a>";
                        ShowModalStaticPro("بازیابی تنظیم", html, 300, 100)
                    } else {
                        mw.Settings = JSON.parse(data);
                        mw.SaveParams();
                        ShowModalStaticPro("بازیابی تنظیم ها", "تنظیم شما بازیابی شد", 300, 100)
                    }
                }
            })
        },
        SaveBasket: function() {
            $.ajax({
                url: MembersSite() + "/tsev2/data/Baskets.aspx",
                type: "POST",
                cache: false,
                crossDomain: true,
                xhrFields: {
                    withCredentials: true
                },
                data: {
                    t: "save",
                    d: JSON.stringify(mw.Settings),
                    dt: 0
                },
                dataType: "html",
                success: function(data) {
                    if (data == "login") {
                        var html = "<a style='text-decoration:underline' href='" + MembersSite() + "/userloginnew.aspx?http://www.tsetmc.com/loader.aspx?ParTree=15131F' target='_top'> برای استفاده از این امکان می بایست عضو شوید و با نام کاربری خود وارد سایت شوید. برای ثبت نام یا ورود به سیستم کلیک کنید</a>";
                        ShowModalStaticPro("ذخیره تنظیم", html, 300, 100)
                    } else {
                        ShowModalStaticPro("ذخیره تنظیم", "تنظیم های شما ذخیره گردید", 300, 100)
                    }
                }
            })
        },
        BuildTemplate: function() {
            HideAllWindow();
            var SettingHTML = "<table class='table1'><tr><th>تعداد ستون ها</th><td><input id='TemplateColNo' style='width:50px' value='" + mw.Settings.CustomTemplate.colNo + "'></td><th>اندازه فونت</th><td><input id='TemplateFontSize' style='width:50px' value='" + mw.Settings.CustomTemplate.fontSize + "'></td><th>ارتفاع سطر ها</th><td><input id='TemplateRowHeight' style='width:50px' value='" + mw.Settings.CustomTemplate.rowHeight + "'></td></tr></table><table class='table1'><tr><th>#</th><th>Title</th><th>Data</th><th>Align</th><th>Color</th><th>Bg Color</th><th>Width</th><th>Style</th><th>Border</th></tr>";
            var ColTitle = "";
            var ColData = "";
            var ColAlign = "";
            var ColColor = "";
            var ColStyle = "";
            var ColWidth = "";
            var ColBackground = "";
            var ColBorder = "";
            var selected = "";
            for (var ipos = 0; ipos < 21; ipos++) {
                var ncol = ColDefault;
                if (mw.Settings.CustomTemplate.cols.length > ipos) {
                    var ncol = jQuery.extend({}, ColDefault, mw.Settings.CustomTemplate.cols[ipos])
                }
                ColTitle = ncol.ColTitle;
                ColData = ncol.ColData;
                ColAlign = ncol.ColAlign;
                ColColor = ncol.ColColor;
                ColStyle = ncol.ColStyle;
                ColWidth = ncol.ColWidth;
                ColBackground = ncol.ColBackground;
                ColBorder = ncol.ColBorder;
                SettingHTML += "<tr><td>" + (ipos + 1) + "</td><td><input id='Col" + ipos + "_Title' value='" + ColTitle + "'></td>";
                SettingHTML += "<td><select id='Col" + ipos + "_Data'>";
                for (var jpos = 0; jpos < TemplateData.length; jpos++) {
                    if (jpos == ColData) {
                        selected = " selected='selected' "
                    } else {
                        selected = ""
                    }
                    SettingHTML += "<option " + selected + " value='" + jpos + "'>" + TemplateData[jpos][1] + "</option>"
                }
                SettingHTML += "</select></td>";
                SettingHTML += "<td><select id='Col" + ipos + "_Align'>";
                for (var jpos = 0; jpos < TemplateAlign.length; jpos++) {
                    if (TemplateAlign[jpos][0] == ColAlign) {
                        selected = " selected='selected' "
                    } else {
                        selected = ""
                    }
                    SettingHTML += "<option " + selected + " value='" + TemplateAlign[jpos][0] + "'>" + TemplateAlign[jpos][1] + "</option>"
                }
                SettingHTML += "</select></td>";
                SettingHTML += "<td><select id='Col" + ipos + "_Color'>";
                for (var jpos = 0; jpos < TemplateColor.length; jpos++) {
                    if (TemplateColor[jpos][0] == ColColor) {
                        selected = " selected='selected' "
                    } else {
                        selected = ""
                    }
                    SettingHTML += "<option " + selected + " style='color:" + TemplateColor[jpos][0] + "' value='" + TemplateColor[jpos][0] + "'>" + TemplateColor[jpos][1] + "</option>"
                }
                SettingHTML += "</select></td>";
                SettingHTML += "<td><select id='Col" + ipos + "_Background'>";
                for (var jpos = 0; jpos < TemplateBackground.length; jpos++) {
                    if (TemplateBackground[jpos][0] == ColBackground) {
                        selected = " selected='selected' "
                    } else {
                        selected = ""
                    }
                    SettingHTML += "<option " + selected + " value='" + TemplateBackground[jpos][0] + "'>" + TemplateBackground[jpos][1] + "</option>"
                }
                SettingHTML += "</select></td>";
                SettingHTML += "<td><input id='Col" + ipos + "_Width' style='width:60px' value='" + ColWidth + "'></td>";
                SettingHTML += "<td><select id='Col" + ipos + "_Style'>";
                for (var jpos = 0; jpos < TemplateStyle.length; jpos++) {
                    if (TemplateStyle[jpos][0] == ColStyle) {
                        selected = " selected='selected' "
                    } else {
                        selected = ""
                    }
                    SettingHTML += "<option " + selected + " style='" + TemplateStyle[jpos][0] + "' value='" + TemplateStyle[jpos][0] + "'>" + TemplateStyle[jpos][1] + "</option>"
                }
                SettingHTML += "</select></td>";
                SettingHTML += "<td><select id='Col" + ipos + "_Border'>";
                for (var jpos = 0; jpos < TemplateBorder.length; jpos++) {
                    if (TemplateBorder[jpos][0] == ColBorder) {
                        selected = " selected='selected' "
                    } else {
                        selected = ""
                    }
                    SettingHTML += "<option " + selected + " style='" + TemplateBorder[jpos][0] + "' value='" + TemplateBorder[jpos][0] + "'>" + TemplateBorder[jpos][1] + "</option>"
                }
                SettingHTML += "</select></td>";
                SettingHTML += "</tr>"
            }
            SettingHTML += "</table><a class='awesome green' href='javascript:mw.SaveTemplate()'>ذخیره قالب شخصی</a>";
            var WinNo = ShowModalStaticPro("ساخت قالب نمایش", SettingHTML)
        },
        SaveTemplate: function() {
            var TemplateColNoVal = $("#TemplateColNo").val();
            TemplateColNoVal = $("<div />").text(TemplateColNoVal).html();
            mw.Settings.CustomTemplate.colNo = parseInt(TemplateColNoVal, 10);
            var TemplateFontSizeVal = $("#TemplateFontSize").val();
            TemplateFontSizeVal = $("<div />").text(TemplateFontSizeVal).html();
            mw.Settings.CustomTemplate.fontSize = parseInt(TemplateFontSizeVal, 10);
            var TemplateRowHeightVal = $("#TemplateRowHeight").val();
            TemplateRowHeightVal = $("<div />").text(TemplateRowHeightVal).html();
            mw.Settings.CustomTemplate.rowHeight = parseInt(TemplateRowHeightVal, 10);
            var ColTitle = "";
            var ColData = "";
            var ColAlign = "";
            var ColColor = "";
            var ColStyle = "";
            var ColWidth = "";
            var ColBackground = "";
            var ColBorder = "";
            for (var ipos = 0; ipos < 21; ipos++) {
                ColTitle = $("<div />").text($("#Col" + ipos + "_Title").val()).html();
                ColData = $("<div />").text($("#Col" + ipos + "_Data").val()).html();
                ColAlign = $("<div />").text($("#Col" + ipos + "_Align").val()).html();
                ColColor = $("<div />").text($("#Col" + ipos + "_Color").val()).html();
                ColStyle = $("<div />").text($("#Col" + ipos + "_Style").val()).html();
                ColBackground = $("<div />").text($("#Col" + ipos + "_Background").val()).html();
                ColWidth = $("<div />").text($("#Col" + ipos + "_Width").val()).html();
                ColBorder = $("<div />").text($("#Col" + ipos + "_Border").val()).html();
                mw.Settings.CustomTemplate.cols[ipos] = {
                    ColTitle: ColTitle,
                    ColData: ColData,
                    ColAlign: ColAlign,
                    ColColor: ColColor,
                    ColStyle: ColStyle,
                    ColWidth: ColWidth,
                    ColBackground: ColBackground,
                    ColBorder: ColBorder
                }
            }
            var ct = mw.Settings.CustomTemplate;
            var TemplateAll = "<style>.t0head{cursor:pointer;border:0px solid #eeeeee;font-size:" + ct.fontSize + "px;direction:ltr;text-align:left;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px}.t0c{border:0px solid #ffffff;font-size:" + ct.fontSize + 'px;direction:ltr;text-align:left;display:inline-block;overflow:hidden;white-space:nowrap;margin:0px;padding:0px;line-height:20px;}.secSep{background-color:rgba(0,170,220,1) !important;;font-size:14px !important;font-weight:bold !important;color:white !important;}.ch1,.ch2,.ch3,.ch4,.ch5,.ch6,.ch7,.ch8{background-color:#ffa5a5}div#main>div:nth-child(2n){background-color:#e2e2e2;}.sr{background-color:#aaaaff !important;}</style><div class="other" id="header" style="white-space:nowrap;position:fixed;top:50px;height:18px;right:3px;left:283px;overflow-y:hidden;overflow-x:hidden;background-color:#eeeeee;z-index:9">';
            var TemplateRowStyle = "cursor:pointer;height:" + ct.rowHeight + "px;white-space:nowrap;line-height:" + ct.rowHeight + "px;";
            var TemplateRow = "";
            var ExcelHeader = "<tr>";
            var ExcelRow = "<tr>";
            for (var ipos = 0; ipos < ct.colNo; ipos++) {
                ColTitle = $("<div />").text($("#Col" + ipos + "_Title").val()).html();
                ColData = $("<div />").text($("#Col" + ipos + "_Data").val()).html();
                ColAlign = $("<div />").text($("#Col" + ipos + "_Align").val()).html();
                ColColor = $("<div />").text($("#Col" + ipos + "_Color").val()).html();
                ColStyle = $("<div />").text($("#Col" + ipos + "_Style").val()).html();
                ColBackground = $("<div />").text($("#Col" + ipos + "_Background").val()).html();
                ColWidth = $("<div />").text($("#Col" + ipos + "_Width").val()).html();
                ColBorder = $("<div />").text($("#Col" + ipos + "_Border").val()).html();
                TemplateAll += '<div style="' + ColStyle + ";" + ColBorder + ";background-color:" + ColBackground + ";text-align:" + ColAlign + ";width:" + ColWidth + "px;text-align:" + ColAlign + '" class="t0head" onclick="mw.ChSortF(\'' + TemplateData[ColData][0] + "')\">" + ColTitle + "</div>";
                ExcelHeader += "<td>" + ColTitle + "<td>";
                if (ColData < 2) {
                    TemplateRow += '<div style="' + ColStyle + ";" + ColBorder + ";background-color:" + ColBackground + ";text-align:" + ColAlign + ";width:" + ColWidth + 'px" class="t0c"><a style=\'color:' + ColColor + ";' class='inst' href='loader.aspx?ParTree=151311&i={i}' target='{i}'>{" + TemplateData[ColData][0] + "}</a></div>"
                } else {
                    if (ColData == 2) {
                        TemplateRow += '<div style="' + ColStyle + ";" + ColBorder + ";background-color:" + ColBackground + ";text-align:" + ColAlign + ";width:" + ColWidth + 'px" class="t0c"><a style=\'color:' + ColColor + ";' class='inst' href='loader.aspx?ParTree=151311&i={i}' target='{i}'>{l18}-{l30}</a></div>"
                    } else {
                        TemplateRow += '<div style="' + ColStyle + ";" + ColBorder + ";text-align:" + ColAlign + ";background-color:" + ColBackground + ";color:" + ColColor + ";width:" + ColWidth + 'px" class="t0c ch{_' + TemplateData[ColData][0] + '}">{' + TemplateData[ColData][0] + "}</div>"
                    }
                }
                ExcelRow += "<td>{" + TemplateData[ColData][0] + "}<td>"
            }
            ExcelHeader += "</tr>";
            ExcelRow += "</tr>";
            TemplateAll += '</div><div class="other" id="main" style="{s};top:68px;left:283px;right:3px;overflow-y:scroll;" onscroll="document.getElementById(\'header\').scrollLeft=document.getElementById(\'main\').scrollLeft"></div><div id="footer"></div>';
            mw.Settings.CustomTemplate.all = TemplateAll;
            mw.Settings.CustomTemplate.rowStyle = TemplateRowStyle;
            mw.Settings.CustomTemplate.row = TemplateRow;
            MWTemplates[MWTemplates.length - 1] = {
                title: "شخصی",
                all: TemplateAll,
                rowStyle: TemplateRowStyle,
                row: TemplateRow,
                excel: {
                    header: ExcelHeader,
                    row: ExcelRow
                }
            };
            mw.PrepareForMobile();
            mw.SaveParams();
            HideAllWindow()
        },
        ShowTemplateWindow: function() {
            var SettingHTML = "";
            for (var ipos = 0; ipos < MWTemplates.length; ipos++) {
                SettingHTML += '<div class="SlideItem" onclick="mw.changeTemplate(' + ipos + ')">' + MWTemplates[ipos].title + "</div>"
            }
            SettingHTML += "<div style='display:inline-block' class='SlideItem' onclick='mw.BuildTemplate()'>ساخت قالب</div><br/>";
            var WinNo = ShowModalStaticPro("قالب نمایش", SettingHTML, 300, 400)
        },
        ShowSortWindow: function() {
            var WinNo = ShowModalStaticPro("مرتب سازی بر اساس", "<div style='direction:rtl;text-align:right;font-size:12px'><ul><li><a href='#' onclick=\"mw.ChSortF('l18');HideAllWindow()\">نماد</a> - <a href='#' onclick=\"mw.ChSortF('l30');HideAllWindow()\">نام</a></li><li><a href='#' onclick=\"mw.ChSortF('tno');HideAllWindow()\">تعداد</a> - <a href='#' onclick=\"mw.ChSortF('tvol');HideAllWindow()\">حجم</a> - <a href='#' onclick=\"mw.ChSortF('tval');HideAllWindow()\">ارزش</a></li><li><a href='#' onclick=\"mw.ChSortF('mv');HideAllWindow()\">ارزش بازار</a></li><li><a href='#' onclick=\"mw.ChSortF('py');HideAllWindow()\">قیمت دیروز</a></li><li><a href='#' onclick=\"mw.ChSortF('pf');HideAllWindow()\">اولین قیمت</a></li><li><a href='#' onclick=\"mw.ChSortF('pl');HideAllWindow()\">آخرین قیمت</a>&nbsp;-&nbsp;<a href='#' onclick=\"mw.ChSortF('plc');HideAllWindow()\">تغییر</a>&nbsp;-&nbsp;<a href='#' onclick=\"mw.ChSortF('plp');HideAllWindow()\">درصد تغییر</a></li><li><a href='#' onclick=\"mw.ChSortF('pc');HideAllWindow()\">قیمت پایانی</a>&nbsp;-&nbsp;<a href='#' onclick=\"mw.ChSortF('pcc');HideAllWindow()\">تغییر</a>&nbsp;-&nbsp;<a href='#' onclick=\"mw.ChSortF('pcp');HideAllWindow()\">درصد تغییر</a></li><li><a href='#' onclick=\"mw.ChSortF('pmin');HideAllWindow()\">کمترین قیمت</a></li><li><a href='#' onclick=\"mw.ChSortF('pmax');HideAllWindow()\">بیشترین قیمت</a></li><li><a href='#' onclick=\"mw.ChSortF('eps');HideAllWindow()\">EPS</a> - <a href='#' onclick=\"mw.ChSortF('pe');HideAllWindow()\">P/E</a></li><li><a href='#' onclick=\"mw.ChSortF('pd1');HideAllWindow()\">قیمت خرید</a> - <a href='#' onclick=\"mw.ChSortF('qd1');HideAllWindow()\">حجم خرید</a></li><li><a href='#' onclick=\"mw.ChSortF('po1');HideAllWindow()\">قیمت فروش</a> - <a href='#' onclick=\"mw.ChSortF('qo1');HideAllWindow()\">حجم فروش</a></li><li><a href='#' onclick=\"mw.ChSortF('visitcount');HideAllWindow()\">تعداد بازدید - پربیننده</a></li><li><a href='#' onclick=\"mw.ChSortF('heven');HideAllWindow()\">زمان آخرین معامله</a></li><li>فیلدهای کاربر <a href='#' onclick=\"mw.ChSortF('cfield0');HideAllWindow()\">cfield0</a> - <a href='#' onclick=\"mw.ChSortF('cfield1');HideAllWindow()\">cfield1</a> -<a href='#' onclick=\"mw.ChSortF('cfield2');HideAllWindow()\">cfield2</a></li></ul>جهت مرتب سازی:<ul><li><a href='#' onclick=\"mw.ChangeSortDir(1);HideAllWindow()\">صعودی</a></li><li><a href='#' onclick=\"mw.ChangeSortDir(-1);HideAllWindow()\">نزولی</a></li></ul></div>", 300, 400)
        },
        ShowAllSettings: function() {
            HideAllWindow();
            var WinNo = ShowModalStaticPro("تنظیمات", "");
            var SettingHTML = "<div class=\"box3\"><div class=\"header\">ذخیره و بازیابی تنظیم ها</div><div style='text-align:center' class=\"content\"><div style='display:inline-block;width:145px' class='awesome red' onclick=\"mw.SaveBasket();\">ذخیره تنظیم ها</div>&nbsp;<div style='display:inline-block;width:145px' class='awesome blue' onclick=\"mw.ListBasket();\">بازیابی تنظیم ها</div>&nbsp;</div><div class=\"header\">سرعت بروز رسانی</div><div class=\"content\"><dl class='ZoomBox'><dd style='width:50px;text-align:center;display:inline-block;vertical-align:top;direction:ltr;'>1 ثانیه</dd><dd style='vertical-align:bottom;display:inline-block;width:750px;direction:ltr'><input type='text' id='UpdateSpeedZoom' width='750px' min='1' max='60'></dd><dd style='width:50px;display:inline-block;text-align:center;vertical-align:top;direction:ltr'>60 ثانیه</dd></dl>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;بروز رسانی هر <input aria-label='سرعت بروزرسانی' type='text' style='width:30px;' id='UpdateSpeedL3'> ثانیه<br/>&nbsp;<input onchange='mw.Settings.ColorChangeEnable=$(\"#ColorChangeEnable\").prop(\"checked\")==true?1:0;mw.SaveParams()' type='checkbox' id='ColorChangeEnable' aria-label='تغییر رنگ زمینه اطلاعات جدید' /> تغییر رنگ زمینه اطلاعات جدید<br/></div><div class=\"header\" style='display:inline-block;'>نحوه نمایش دیده بان بازار؟</div>";
            mw.Settings.ViewMode == 0 ? cls = "" : cls = "tra";
            SettingHTML += "<div style='display:inline-block;width:150px' role='checkbox' aria-checked='" + (mw.Settings.ViewMode == 0 ? "true" : "false") + "' aria-label='نمایش همه نمادها در دیده بان'  class='awesome " + cls + "' onclick=\"mw.Settings.SectorNo='';mw.Settings.BasketNo=-1;mw.Settings.ViewMode=0;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.RemoveAllData();mw.RenderData();\">همه نمادها</div>&nbsp;";
            mw.Settings.ViewMode == 1 ? cls = "" : cls = "tra";
            SettingHTML += "<div style='display:inline-block;width:150px' role='checkbox' aria-checked='" + (mw.Settings.ViewMode == 1 ? "true" : "false") + "' aria-label='نمایش فقط نمادهای معامله شده در دیده بان'  class='awesome " + cls + "' onclick=\"mw.Settings.SectorNo='';mw.Settings.BasketNo=-1;mw.Settings.ViewMode=1;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.RemoveAllData();mw.RenderData();\">نمادهای معامله شده</div>&nbsp;";
            if (mw.Settings.ViewMode == 2) {
                SettingHTML += "<div style='display:inline-block;width:150px' class='awesome'>نمایش سبد</div>&nbsp;"
            }
            if (mw.Settings.ViewMode == 3) {
                SettingHTML += "<div style='display:inline-block;width:150px' class='awesome'>نمایش گروه</div>"
            }
            SettingHTML += "<br/><br/>";
            SettingHTML += "<div style='display:inline-block;' class=\"header\">بازار انتخابی برای نمایش</div>";
            mw.Settings.Market == 0 ? cls = "" : cls = "tra";
            SettingHTML += "<div style='display:inline-block;width:140px' role='checkbox' aria-checked='" + (mw.Settings.Market == 0 ? "true" : "false") + "' aria-label='نمایش هر دو بازار بورس و فرابورس در دیده بان'  class='awesome " + cls + '\' onclick="mw.Settings.Market=0;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.RemoveAllData();mw.RenderData();">بورس و فرابورس</div>&nbsp;';
            mw.Settings.Market == 1 ? cls = "" : cls = "tra";
            SettingHTML += "<div style='display:inline-block;width:110px' role='checkbox' aria-checked='" + (mw.Settings.Market == 1 ? "true" : "false") + "' aria-label='نمایش فقط بازار بورس در دیده بان'  class='awesome " + cls + '\' onclick="mw.Settings.Market=1;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.RemoveAllData();mw.RenderData();">بازار بورس</div>&nbsp;';
            mw.Settings.Market == 2 ? cls = "" : cls = "tra";
            SettingHTML += "<div style='display:inline-block;width:110px' role='checkbox' aria-checked='" + (mw.Settings.Market == 2 ? "true" : "false") + "' aria-label='نمایش فقط بازار فرابورس در دیده بان'  class='awesome " + cls + '\' onclick="mw.Settings.Market=2;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.RemoveAllData();mw.RenderData();">بازار فرابورس</div>&nbsp;';
            SettingHTML += "<br/><br/>";
            SettingHTML += "<div style='display:inline-block;' class=\"header\">گروه بندی گروه های صنعت</div>";
            mw.Settings.GroupBySector == 0 ? cls = "" : cls = "tra";
            SettingHTML += "<div style='display:inline-block;width:60px' role='checkbox' aria-checked='" + (mw.Settings.GroupBySector == 0 ? "true" : "false") + "' aria-label='گروه بندی گروه های صنعت در دیده بان - خیر'  class='awesome " + cls + '\' onclick="mw.Settings.GroupBySector=0;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.RemoveAllData();mw.RenderData();mw.SortData();">خیر</div>&nbsp;';
            mw.Settings.GroupBySector == 1 ? cls = "" : cls = "tra";
            SettingHTML += "<div style='display:inline-block;width:60px' role='checkbox' aria-checked='" + (mw.Settings.GroupBySector == 1 ? "true" : "false") + "' aria-label='گروه بندی گروه های صنعت در دیده بان - بلی'  class='awesome " + cls + '\' onclick="mw.Settings.GroupBySector=1;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.RemoveAllData();mw.RenderData();mw.SortData();">بلی</div>&nbsp;';
            SettingHTML += "<br/><br/>";
            SettingHTML += "<div style='display:inline-block;' class=\"header\">چرخش خودکار</div>";
            mw.Settings.AutoScroll == 0 ? cls = "" : cls = "tra";
            SettingHTML += "<div style='display:inline-block;width:60px' role='checkbox' aria-checked='" + (mw.Settings.AutoScroll == 0 ? "true" : "false") + "' aria-label='چرخش خودکار دیده بان - خیر'  class='awesome " + cls + '\' onclick="mw.Settings.AutoScroll=0;mw.AutoScroll(false);mw.SaveParams();HideAllWindow()">خیر</div>&nbsp;';
            mw.Settings.AutoScroll == 1 ? cls = "" : cls = "tra";
            SettingHTML += "<div style='display:inline-block;width:60px' role='checkbox' aria-checked='" + (mw.Settings.AutoScroll == 1 ? "true" : "false") + "' aria-label='چرخش خودکار دیده بان - بلی'  class='awesome " + cls + '\' onclick="mw.Settings.AutoScroll=1;mw.AutoScroll(true);mw.SaveParams();HideAllWindow()">بلی</div>&nbsp;';
            SettingHTML += "<br/><br/>";
            SettingHTML += "<div style='display:inline-block;' class=\"header\">نحوه نمایش اعداد بزرگ</div>";
            mw.Settings.BigNumberSymbol == 0 ? cls = "" : cls = "tra";
            SettingHTML += "<div style='display:inline-block;width:60px' role='checkbox' aria-checked='" + (mw.Settings.BigNumberSymbol == 0 ? "true" : "false") + "' aria-label='نمایش اعداد به صورت ساده' class='awesome " + cls + '\' onclick="mw.Settings.BigNumberSymbol=0;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.RemoveAllData();mw.RenderData();mw.SortData();">نمایش ساده</div>&nbsp;';
            mw.Settings.BigNumberSymbol == 1 ? cls = "" : cls = "tra";
            SettingHTML += "<div style='display:inline-block;width:160px'  role='checkbox' aria-checked='" + (mw.Settings.BigNumberSymbol == 1 ? "true" : "false") + "' aria-label='M نمایش اعداد به صورت (میلیون) B (میلیارد)'  class='awesome " + cls + '\' onclick="mw.Settings.BigNumberSymbol=1;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.RemoveAllData();mw.RenderData();mw.SortData();">نمایش M (میلیون) B (میلیارد)</div>&nbsp;';
            SettingHTML += "<br/><hr/>";
            SettingHTML += "<div style='display:inline-block;' class=\"header\">نوع اوراق</div>";
            mw.Settings.ShowSaham == 1 ? cls = "" : cls = "tra";
            SettingHTML += "<div aria-live='assertive'  role='checkbox' aria-checked='" + (mw.Settings.ShowSaham == 1 ? "true" : "false") + "' aria-label='نمایش اوراق سهام در دیده بان' style='display:inline-block;width:120px' class='awesome " + cls + '\' onclick="mw.Settings.ShowSaham=1-mw.Settings.ShowSaham;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();">سهام</div>&nbsp;';
            mw.Settings.ShowPayeFarabourse == 1 ? cls = "" : cls = "tra";
            SettingHTML += "<div role='checkbox' aria-checked='" + (mw.Settings.ShowPayeFarabourse == 1 ? "true" : "false") + "' aria-label='نمایش اوراق بازار پایه در دیده بان'  style='display:inline-block;width:120px' class='awesome " + cls + '\' onclick="mw.Settings.ShowPayeFarabourse=1-mw.Settings.ShowPayeFarabourse;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();">فرابورس - بازار پایه</div>&nbsp;';
            mw.Settings.ShowHousingFacilities == 1 ? cls = "" : cls = "tra";
            SettingHTML += "<div role='checkbox' aria-checked='" + (mw.Settings.ShowHousingFacilities == 1 ? "true" : "false") + "' aria-label='نمایش اوراق تسهیلات مسکن در دیده بان'  style='display:inline-block;width:120px' class='awesome " + cls + '\' onclick="mw.Settings.ShowHousingFacilities=1-mw.Settings.ShowHousingFacilities;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();">تسهیلات مسکن</div>&nbsp;';
            mw.Settings.ShowHaghTaghaddom == 1 ? cls = "" : cls = "tra";
            SettingHTML += "<div role='checkbox' aria-checked='" + (mw.Settings.ShowHaghTaghaddom == 1 ? "true" : "false") + "' aria-label='نمایش اوراق حق تقدم در دیده بان'  style='display:inline-block;width:120px' class='awesome " + cls + '\' onclick="mw.Settings.ShowHaghTaghaddom=1-mw.Settings.ShowHaghTaghaddom;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();">حق تقدم</div>&nbsp;';
            mw.Settings.ShowOraghMosharekat == 1 ? cls = "" : cls = "tra";
            SettingHTML += "<div role='checkbox' aria-checked='" + (mw.Settings.ShowOraghMosharekat == 1 ? "true" : "false") + "' aria-label='نمایش اوراق بدهی در دیده بان'  style='display:inline-block;width:120px' class='awesome " + cls + '\' onclick="mw.Settings.ShowOraghMosharekat=1-mw.Settings.ShowOraghMosharekat;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();">اوراق بدهی</div>&nbsp;';
            mw.Settings.ShowEkhtiarForoush == 1 ? cls = "" : cls = "tra";
            SettingHTML += "<div role='checkbox' aria-checked='" + (mw.Settings.ShowEkhtiarForoush == 1 ? "true" : "false") + "' aria-label='نمایش اوراق اختیار معامله در دیده بان'  style='display:inline-block;width:120px' class='awesome " + cls + '\' onclick="mw.Settings.ShowEkhtiarForoush=1-mw.Settings.ShowEkhtiarForoush;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();">اختیار معامله</div>&nbsp;';
            mw.Settings.ShowAti == 1 ? cls = "" : cls = "tra";
            SettingHTML += "<div role='checkbox' aria-checked='" + (mw.Settings.ShowAti == 1 ? "true" : "false") + "' aria-label='نمایش اوراق آتی در دیده بان'  style='display:inline-block;width:120px' class='awesome " + cls + '\' onclick="mw.Settings.ShowAti=1-mw.Settings.ShowAti;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();">آتی</div>&nbsp;';
            mw.Settings.ShowSandoogh == 1 ? cls = "" : cls = "tra";
            SettingHTML += "<div role='checkbox' aria-checked='" + (mw.Settings.ShowSandoogh == 1 ? "true" : "false") + "' aria-label='نمایش صندوق های سرمایه گذاری در دیده بان'  style='display:inline-block;width:120px' class='awesome " + cls + '\' onclick="mw.Settings.ShowSandoogh=1-mw.Settings.ShowSandoogh;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();">صندوق سرمایه گذاری </div>&nbsp;';
            mw.Settings.ShowKala == 1 ? cls = "" : cls = "tra";
            SettingHTML += "<div role='checkbox' aria-checked='" + (mw.Settings.ShowKala == 1 ? "true" : "false") + "' aria-label='نمایش بورس کالا در دیده بان' style='display:inline-block;width:120px' class='awesome " + cls + '\' onclick="mw.Settings.ShowKala=1-mw.Settings.ShowKala;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.ShowAllSettings();mw.RemoveAllData();mw.RenderData();mw.SortData();">بورس کالا </div>&nbsp;';
            SettingHTML += "<br/><hr/>";
            SettingHTML += "<div style='display:inline-block;' class=\"header\">اطلاعات تکمیلی</div>";
            mw.Settings.LoadClientType == 1 ? cls = "" : cls = "tra";
            SettingHTML += "<div role='checkbox' aria-checked='" + (mw.Settings.LoadClientType == 1 ? "true" : "false") + "' aria-label='بارگذاری اطلاعات حقیقی حقوقی' style='display:inline-block;width:150px' class='awesome " + cls + '\' onclick="mw.Settings.LoadClientType=1-mw.Settings.LoadClientType;mw.SaveParams();HideAllWindow();mw.LoadClientType();">حقیقی و حقوقی</div>&nbsp;';
            mw.Settings.LoadInstStat == 1 ? cls = "" : cls = "tra";
            SettingHTML += "<div role='checkbox' aria-checked='" + (mw.Settings.LoadInstStat == 1 ? "true" : "false") + "' aria-label='بارگذاری آمارهای کلیدی'  style='display:inline-block;width:150px' class='awesome " + cls + '\' onclick="mw.Settings.LoadInstStat=1-mw.Settings.LoadInstStat;mw.SaveParams();HideAllWindow();mw.LoadInstStat();">آمارهای کلیدی</div>&nbsp;';
            mw.Settings.LoadInstHistory == 1 ? cls = "" : cls = "tra";
            SettingHTML += "<div role='checkbox' aria-checked='" + (mw.Settings.LoadInstHistory == 1 ? "true" : "false") + "' aria-label='بارگذاری تاریخچه قیمت ها'  style='display:inline-block;width:150px' class='awesome " + cls + '\' onclick="mw.Settings.LoadInstHistory=1-mw.Settings.LoadInstHistory;mw.SaveParams();HideAllWindow();mw.LoadInstHistory();">تاریخچه قیمت ها</div>&nbsp;';
            SettingHTML += "<br/>";
            if (mw.Settings.Baskets.length != 0) {
                SettingHTML += '<hr/><br/><div class="header">سبد انتخابی برای نمایش</div><div style=\'text-align:center\' class="content">';
                for (var ipos = 0; ipos < mw.Settings.Baskets.length; ipos++) {
                    mw.Settings.ViewMode == 2 && mw.Settings.BasketNo == ipos ? cls = "" : cls = "tra";
                    SettingHTML += "<div class='awesome " + cls + "' style='display:inline-block;width:150px' onclick=\"mw.Settings.ViewMode=2;mw.Settings.BasketNo=" + ipos + ';mw.BasketInsts = mw.Settings.Baskets[mw.Settings.BasketNo].Instruments;mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.RemoveAllData();mw.RenderData();">' + mw.Settings.Baskets[ipos].BasketName + " - " + mw.NumberOfInstruments(ipos) + "</div>&nbsp;"
                }
            }
            SettingHTML += "</div><hr/>";
            var selected = "";
            SettingHTML += "<div style='display:inline-block;' class=\"header\">گروه انتخابی برای نمایش</div>";
            SettingHTML += "<select aria-label='گروه انتخاب برای نمایش' style='font-family:tahoma' id='SectorList' onchange=\"mw.Settings.ViewMode=3;mw.Settings.SectorNo=$('#SectorList').val();mw.SaveParams();mw.ShowSettings();HideAllWindow();mw.RemoveAllData();mw.RenderData();\">";
            if (mw.Settings.ViewMode != 3) {
                SettingHTML += "<option selected='selected' value=''>-----</option>"
            }
            for (var ipos = 0; ipos < Sectors.length; ipos++) {
                mw.Settings.ViewMode == 3 && mw.Settings.SectorNo == Sectors[ipos][0] ? selected = "selected='selected'" : selected = "";
                SettingHTML += "<option " + selected + " value='" + Sectors[ipos][0] + "'>" + Sectors[ipos][1] + "</option>"
            }
            SettingHTML += "</select><br/><hr/>";
            SettingHTML += "</div>";
            $("#ModalWindowInner" + WinNo).append(SettingHTML);
            $("#UpdateSpeedZoom").range({
                range: false,
                passedID: "UpdateSpeedZoomCursor",
                values: [mw.Settings.UpdateSpeed / 1000],
                change: function() {},
                blur: function() {
                    mw.Settings.UpdateSpeed = parseInt($("#UpdateSpeedZoom").val(), 10) * 1000;
                    mw.SaveParams();
                    $("#UpdateSpeedL3").val(mw.Settings.UpdateSpeed / 1000);
                    mw.ShowSettings()
                }
            });
            $("#UpdateSpeedL3").val(mw.Settings.UpdateSpeed / 1000);
            if (mw.Settings.ColorChangeEnable == 1) {
                $("#ColorChangeEnable").prop("checked", true)
            } else {
                $("#ColorChangeEnable").prop("checked", false)
            }
            $("#UpdateSpeedL3").on("keyup", function() {
                this.value = this.value.replace(/[^0-9]/gi, "")
            });
            $("#UpdateSpeedL3").change(function() {
                mw.Settings.UpdateSpeed = parseInt($("#UpdateSpeedL3").val(), 10) * 1000;
                mw.SaveParams();
                mw.ShowSettings()
            })
        },
        SelectFilter: function(FilterNo) {
            if (FilterNo == -1 || FilterNo >= mw.Settings.Filters.length || mw.Settings.Filters.length == 0) {
                mw.FilterCode = "";
                mw.Settings.FilterNo = -1;
                mw.RemoveAllData();
                mw.RenderData();
                return
            }
            mw.FilterCode = mw.PrepareFilterCode(mw.Settings.Filters[FilterNo].FilterCode);
            mw.Settings.FilterNo = FilterNo;
            mw.RemoveAllData();
            mw.RenderData()
        },
        PrepareFilterCode: function(RawCode) {
            var FilterCode = RawCode;
            FilterCode = FilterCode.replace(/\x28l18\x29/g, 'row["l18"]');
            FilterCode = FilterCode.replace(/\x28l30\x29/g, 'row["l30"]');
            FilterCode = FilterCode.replace(/\x28tno\x29/g, 'parseInt(row["tno"],10)');
            FilterCode = FilterCode.replace(/\x28tvol\x29/g, 'parseInt(row["tvol"],10)');
            FilterCode = FilterCode.replace(/\x28tval\x29/g, 'parseInt(row["tval"],10)');
            FilterCode = FilterCode.replace(/\x28py\x29/g, 'parseFloat(row["py"])');
            FilterCode = FilterCode.replace(/\x28pf\x29/g, 'parseFloat(row["pf"])');
            FilterCode = FilterCode.replace(/\x28pmin\x29/g, 'parseFloat(row["pmin"])');
            FilterCode = FilterCode.replace(/\x28pmax\x29/g, 'parseFloat(row["pmax"])');
            FilterCode = FilterCode.replace(/\x28pl\x29/g, 'parseFloat(row["pl"])');
            FilterCode = FilterCode.replace(/\x28plc\x29/g, 'parseFloat(row["plc"])');
            FilterCode = FilterCode.replace(/\x28plp\x29/g, 'parseFloat(row["plp"])');
            FilterCode = FilterCode.replace(/\x28pc\x29/g, 'parseFloat(row["pc"])');
            FilterCode = FilterCode.replace(/\x28pcc\x29/g, 'parseFloat(row["pcc"])');
            FilterCode = FilterCode.replace(/\x28pcp\x29/g, 'parseFloat(row["pcp"])');
            FilterCode = FilterCode.replace(/\x28eps\x29/g, 'parseFloat(row["eps"])');
            FilterCode = FilterCode.replace(/\x28pe\x29/g, 'parseFloat(row["pe"])');
            FilterCode = FilterCode.replace(/\x28pd1\x29/g, 'parseFloat(row["pd1"])');
            FilterCode = FilterCode.replace(/\x28zd1\x29/g, 'parseFloat(row["zd1"])');
            FilterCode = FilterCode.replace(/\x28qd1\x29/g, 'parseFloat(row["qd1"])');
            FilterCode = FilterCode.replace(/\x28po1\x29/g, 'parseFloat(row["po1"])');
            FilterCode = FilterCode.replace(/\x28zo1\x29/g, 'parseFloat(row["zo1"])');
            FilterCode = FilterCode.replace(/\x28qo1\x29/g, 'parseFloat(row["qo1"])');
            FilterCode = FilterCode.replace(/\x28pd2\x29/g, 'parseFloat(row["pd2"])');
            FilterCode = FilterCode.replace(/\x28zd2\x29/g, 'parseFloat(row["zd2"])');
            FilterCode = FilterCode.replace(/\x28qd2\x29/g, 'parseFloat(row["qd2"])');
            FilterCode = FilterCode.replace(/\x28po2\x29/g, 'parseFloat(row["po2"])');
            FilterCode = FilterCode.replace(/\x28zo2\x29/g, 'parseFloat(row["zo2"])');
            FilterCode = FilterCode.replace(/\x28qo2\x29/g, 'parseFloat(row["qo2"])');
            FilterCode = FilterCode.replace(/\x28pd3\x29/g, 'parseFloat(row["pd3"])');
            FilterCode = FilterCode.replace(/\x28zd3\x29/g, 'parseFloat(row["zd3"])');
            FilterCode = FilterCode.replace(/\x28qd3\x29/g, 'parseFloat(row["qd3"])');
            FilterCode = FilterCode.replace(/\x28po3\x29/g, 'parseFloat(row["po3"])');
            FilterCode = FilterCode.replace(/\x28zo3\x29/g, 'parseFloat(row["zo3"])');
            FilterCode = FilterCode.replace(/\x28qo3\x29/g, 'parseFloat(row["qo3"])');
            FilterCode = FilterCode.replace(/\x28bvol\x29/g, 'parseInt(row["bvol"],10)');
            FilterCode = FilterCode.replace(/\x28cs\x29/g, 'parseInt(row["cs"],10)');
            FilterCode = FilterCode.replace(/\x28tmax\x29/g, 'parseFloat(row["tmax"])');
            FilterCode = FilterCode.replace(/\x28tmin\x29/g, 'parseFloat(row["tmin"])');
            FilterCode = FilterCode.replace(/\x28z\x29/g, 'parseInt(row["z"],10)');
            FilterCode = FilterCode.replace(/\x28mv\x29/g, 'parseFloat(row["mv"])');
            FilterCode = FilterCode.replace(/\x28cfield0\x29/g, 'row["cfield0"]');
            FilterCode = FilterCode.replace(/\x28cfield1\x29/g, 'row["cfield1"]');
            FilterCode = FilterCode.replace(/\x28cfield2\x29/g, 'row["cfield2"]');
            FilterCode = FilterCode.replace(/\x28ct\x29/g, 'mw.ClientType[row["inscode"]]');
            FilterCode = FilterCode.replace(/\x5Bis/g, 'mw.InstStat[row["inscode"]][');
            FilterCode = FilterCode.replace(/\x5Bih\x5D/g, 'mw.InstHistory[row["inscode"]]');
            return FilterCode
        },
        StartMarketWatch: function() {
            $(document).keypress(function(event) {
                if ((event.which == 83 || event.which == 115) && (document.activeElement == null || (document.activeElement.tagName != "INPUT" && document.activeElement.tagName != "TEXTAREA"))) {
                    mw.ShowAllSettings()
                }
            });
            $("#pulldown").remove();
            $("#FastView").css("left", "20px").css("margin-left", "0px");
            mw.Settings = mw.DefaultSettings;
            var TmpSettings = getData("MarketWatchSettings");
            if (TmpSettings != null) {
                jQuery.extend(mw.Settings, JSON.parse(TmpSettings))
            }
            if (typeof mw.field[mw.Settings.sortField] == "undefined") {
                mw.Settings.sortField = "tno"
            }
            if (mw.Settings.ViewMode == 2 && mw.Settings.BasketNo == -1) {
                mw.Settings.BasketNo = -1;
                mw.Settings.ViewMode = 0;
                mw.SaveParams()
            }
            if (mw.Settings.BasketNo != -1) {
                if (mw.Settings.BasketNo >= mw.Settings.Baskets.length) {
                    mw.Settings.BasketNo = -1;
                    mw.Settings.ViewMode = 0;
                    mw.SaveParams()
                } else {
                    mw.BasketInsts = mw.Settings.Baskets[mw.Settings.BasketNo].Instruments
                }
            }
            $(document.body).append("<div id='infop' style='direction:rtl;font-size:12px;text-align:right;border-right:2px solid black;position:fixed;top:50px;overflow:auto;bottom:0px;width:280px;left:3px;background-color:#ffffdd'><div class='MwText' style='width:100%;height:25px;margin:5px;display:flex;justify-content: right;font:normal bold 11px/22px Tahoma,sans-serif;' ><div id='userFullName'></div><br/><a id='userLink' style='margin-right:10px;'></a></div> <div id='infotab' style='text-align:center;'></div><div id='infos' class='rainbow_inf_elm'></div><div id='infoc'class='rainbow_inf_elm'><div id='RoomName' onclick='tw.ChooseRoomUI()'>نام کلاس: برای انتخاب کلاس کلیک کنید</div><input id='twsendbox' onkeypress='tw.SendBoxKeyPress(event)' class='twbox'/><div id='twviewer'/></div></div>");
            DrawRainbowTab({
                tabName: "inf",
                tabPlace: "#infotab",
                firstColor: 3,
                RememberLastTab: "1",
                item: [{
                    Title: "اطلاعات نماد",
                    RelatedElement: "#infos",
                    OnShowFunction: ""
                }, {
                    Title: "کلاس های خصوصی",
                    RelatedElement: "#infoc",
                    OnShowFunction: ""
                }]
            });
            $(document.body).append("<div id='SettingsDesc' class='slideStatic' style='width:650px;left:330px;margin-left:0px;background-color:#ccddff;text-align:right'></div>");
            mw.ShowSettings();
            setData("ActiveTab", "MW");
            $(window).focus(function() {
                setData("ActiveTab", "MW")
            });
            MWTemplates[MWTemplates.length - 1] = {
                title: "شخصی",
                all: mw.Settings.CustomTemplate.all,
                rowStyle: mw.Settings.CustomTemplate.rowStyle,
                row: mw.Settings.CustomTemplate.row
            };
            mw.PrepareForMobile();
            $("#display").html(MWTemplates[mw.Settings.ActiveTemplate].all);
            mw.SetPreviewDefault();
            mw.SelectFilter(mw.Settings.FilterNo);
            ShowFastView();
            mw.UpdateMarketWatch();
            mw.getUser();
            if (mw.Settings.LoadClientType == 1) {
                mw.LoadClientType()
            }
            if (mw.Settings.LoadInstStat == 1) {
                mw.LoadInstStat()
            }
            if (mw.Settings.LoadInstHistory == 1) {
                mw.LoadInstHistory()
            }
            tw.StartEngine();
            if (mw.Settings.AutoScroll == 1) {
                mw.AutoScroll(true)
            }
        },
        PrepareForMobile: function() {
            var ismobile = navigator.userAgent.match(/(iPad)|(iPhone)|(iPod)|(android)|(webOS)/i);
            for (var ipos = 0; ipos < MWTemplates.length; ipos++) {
                if (ismobile == null) {
                    MWTemplates[ipos].all = MWTemplates[ipos].all.replace("{s}", "bottom:2px;overflow-x:auto;position:fixed")
                } else {
                    MWTemplates[ipos].all = MWTemplates[ipos].all.replace("{s}", "position:absolute")
                }
            }
        },
        AddNewRowToStore: function(RowID, defaultData) {
            if (typeof mw.AllRows[RowID] == "undefined") {
                mw.AllRows[RowID] = defaultData
            }
        },
        PreSelectedRow: 0,
        SelectedRow: 0,
        ChangeRowList: [],
        AddDataToStore: function(RowID, data) {
            if (typeof mw.AllRows[RowID] == "undefined") {
                return
            }
            for (var key in data) {
                if (mw.AllRows[RowID][key] == data[key]) {
                    mw.AllRows[RowID]["_" + key] = "0"
                } else {
                    mw.AllRows[RowID]["_" + key] = "" + mw.RoundNo
                }
                mw.AllRows[RowID][key] = data[key]
            }
        },
        ResetChangeInStore: function() {
            var ipos;
            var elm;
            for (ipos = 0; ipos < mw.ChangeRowList.length; ipos++) {
                elm = mw.AllRows[mw.ChangeRowList[ipos]];
                if (typeof elm != "undefined") {
                    elm._heven = "0";
                    elm._pc = "0";
                    elm._pcc = "0";
                    elm._pcp = "0";
                    elm._pl = "0";
                    elm._plc = "0";
                    elm._plp = "0";
                    elm._tno = "0";
                    elm._tvol = "0";
                    elm._tval = "0";
                    elm._pmin = "0";
                    elm._pmax = "0";
                    elm._eps = "0";
                    elm._pe = "0";
                    elm._zo1 = "0";
                    elm._zd1 = "0";
                    elm._pd1 = "0";
                    elm._po1 = "0";
                    elm._qd1 = "0";
                    elm._qo1 = "0";
                    elm._zo2 = "0";
                    elm._zd2 = "0";
                    elm._pd2 = "0";
                    elm._po2 = "0";
                    elm._qd2 = "0";
                    elm._qo2 = "0";
                    elm._zo3 = "0";
                    elm._zd3 = "0";
                    elm._pd3 = "0";
                    elm._po3 = "0";
                    elm._qd3 = "0";
                    elm._qo3 = "0"
                }
            }
            mw.ChangeRowList = []
        },
        SaveSettings: function(all, basketNo, WinNo) {
            mw.Settings.AllTrade = all;
            mw.Settings.BasketNo = basketNo;
            mw.heven = 0;
            mw.refid = 0;
            if (basketNo != -1) {
                mw.BasketInsts = mw.Settings.Baskets[basketNo].Instruments;
                if (mw.BasketInsts == null) {
                    setData("Basket" + basketNo, "");
                    mw.BasketInsts = ""
                }
            }
            mw.SaveParams();
            mw.RenderData()
        },
        logOutUser: function() {
            $.ajax({
                url: MembersSite() + "/tsev2/data/MarketWatchInit.aspx",
                data: {
                    c: "logoutuser"
                },
                type: "POST",
                cache: false,
                xhrFields: {
                    withCredentials: true
                },
                dataType: "html",
                timeout: 10000,
                crossDomain: true,
                success: function() {
                    mw.userFullName = undefined
                }
            })
        },
        getUser: function() {
            $.ajax({
                url: MembersSite() + "/tsev2/data/MarketWatchInit.aspx",
                type: "POST",
                cache: false,
                xhrFields: {
                    withCredentials: true
                },
                data: {
                    c: "userinfo"
                },
                dataType: "html",
                timeout: 10000,
                crossDomain: true,
                success: function(data) {
                    mw.userFullName = data
                }
            })
        },
        UpdateMarketWatch: function() {
            mw.UpdateCounter++;
            if (getData("ActiveTab") != "MW" && mw.FilterCode.length == 0 && mw.UpdateCounter % 5 != 0) {
                var t1 = mw.Settings.UpdateSpeed;
                if (typeof timer1 != "undefined") {
                    window.clearTimeout(timer1)
                }
                timer1 = window.setTimeout("mw.UpdateMarketWatch()", 1000);
                mw.UpdateIgnore++;
                return
            }
            $.ajax({
                url: mw.heven == 0 ? "tsev2/data/MarketWatchInit.aspx" : "tsev2/data/MarketWatchPlus.aspx",
                cache: true,
                data: {
                    h: 5 * Math.floor(mw.heven / 5),
                    r: 25 * Math.floor(mw.refid / 25)
                },
                dataType: "html",
                timeout: 10000,
                error: function() {
                    if (typeof timer1 != "undefined") {
                        window.clearTimeout(timer1)
                    }
                    timer1 = window.setTimeout("mw.UpdateMarketWatch()", 600)
                },
                success: function(data) {
                    if (++mw.RoundNo > 8) {
                        mw.RoundNo = 1
                    }
                    var all = data.split("@");
                    var ActiveTab = getData("ActiveTab");
                    HandleMsg(all[0]);
                    if (all[1].length != 0) {
                        UpdateFastView(all[1].split(","))
                    }
                    var InstPrice = all[2].split(";");
                    for (ipos = 0; ipos < InstPrice.length; ipos++) {
                        var col = InstPrice[ipos].split(",");
                        var RowID = col[0];
                        if (col.length == 10) {
                            if (typeof mw.AllRows[RowID] == "undefined") {} else {
                                var py = parseInt(mw.AllRows[RowID]["py"]);
                                var eps = mw.AllRows[RowID]["eps"];
                                mw.AddDataToStore(RowID, {
                                    heven: col[1],
                                    pf: col[2],
                                    pc: col[3],
                                    pcc: "" + parseInt(col[3]) - py,
                                    pcp: "" + AdvRound(100 * (parseInt(col[3]) - py) / py, 2),
                                    pl: col[4],
                                    plc: col[5] == "0" ? "0" : "" + parseInt(col[4]) - py,
                                    plp: col[5] == "0" ? "0" : "" + AdvRound(100 * (parseInt(col[4]) - py) / py, 2),
                                    tno: col[5],
                                    tvol: col[6],
                                    tval: col[7],
                                    pmin: col[8],
                                    pmax: col[9],
                                    pe: eps == "" ? "" : AdvRound(parseInt(col[4]) / parseInt(eps), 2),
                                    render: "",
                                    preview: ""
                                });
                                mw.ChangeRowList.push(RowID);
                                if (mw.preOpen == true && col[5] != "0") {
                                    mw.preOpen = false
                                }
                                if (mw.heven < parseInt(col[1])) {
                                    mw.heven = parseInt(col[1])
                                }
                            }
                        } else {
                            mw.AddNewRowToStore(RowID, {
                                inscode: col[0],
                                iid: col[1],
                                l18: col[2],
                                l30: col[3],
                                py: col[13],
                                bvol: col[15],
                                visitcount: col[16],
                                flow: col[17],
                                cs: col[18],
                                tmax: col[19],
                                tmin: col[20],
                                z: col[21],
                                yval: col[22],
                                zo1: "",
                                zd1: "",
                                pd1: "",
                                po1: "",
                                qd1: "",
                                qo1: "",
                                _zo1: "",
                                _zd1: "",
                                _pd1: "",
                                _po1: "",
                                _qd1: "",
                                _qo1: "",
                                zo2: "",
                                zd2: "",
                                pd2: "",
                                po2: "",
                                qd2: "",
                                qo2: "",
                                _zo2: "",
                                _zd2: "",
                                _pd2: "",
                                _po2: "",
                                _qd2: "",
                                _qo2: "",
                                zo3: "",
                                zd3: "",
                                pd3: "",
                                po3: "",
                                qd3: "",
                                qo3: "",
                                _zo3: "",
                                _zd3: "",
                                _pd3: "",
                                _po3: "",
                                _qd3: "",
                                _qo3: "",
                                render: "",
                                preview: "",
                                cfield0: "",
                                cfield1: "",
                                cfield2: ""
                            });
                            mw.AddDataToStore(RowID, {
                                heven: col[4],
                                pf: col[5],
                                pc: col[6],
                                pcc: "" + parseInt(col[6]) - parseInt(col[13]),
                                pcp: "" + AdvRound(100 * (parseInt(col[6]) - parseInt(col[13])) / parseInt(col[13]), 2),
                                pl: col[7],
                                plc: col[8] == "0" ? "0" : "" + parseInt(col[7]) - parseInt(col[13]),
                                plp: col[8] == "0" ? "0" : "" + AdvRound(100 * (parseInt(col[7]) - parseInt(col[13])) / parseInt(col[13]), 2),
                                tno: col[8],
                                tvol: col[9],
                                tval: col[10],
                                pmin: col[11],
                                pmax: col[12],
                                eps: col[14],
                                pe: col[14] == "" ? "" : AdvRound(parseInt(col[6]) / parseInt(col[14]), 2)
                            });
                            mw.ChangeRowList.push(RowID);
                            if (mw.preOpen == true && col[8] != "0") {
                                mw.preOpen = false
                            }
                            if (mw.heven < parseInt(col[4])) {
                                mw.heven = parseInt(col[4])
                            }
                        }
                    }
                    var BestLimit = all[3].split(";");
                    for (ipos = 0; ipos < BestLimit.length; ipos++) {
                        var col = BestLimit[ipos].split(",");
                        var RowID = col[0];
                        if (typeof mw.AllRows[RowID] == "undefined") {
                            continue
                        }
                        var data;
                        switch (col[1]) {
                        case "1":
                            data = {
                                zo1: col[2],
                                zd1: col[3],
                                pd1: col[4],
                                po1: col[5],
                                qd1: col[6],
                                qo1: col[7],
                                render: "",
                                preview: ""
                            };
                            break;
                        case "2":
                            data = {
                                zo2: col[2],
                                zd2: col[3],
                                pd2: col[4],
                                po2: col[5],
                                qd2: col[6],
                                qo2: col[7],
                                render: "",
                                preview: ""
                            };
                            break;
                        case "3":
                            data = {
                                zo3: col[2],
                                zd3: col[3],
                                pd3: col[4],
                                po3: col[5],
                                qd3: col[6],
                                qo3: col[7],
                                render: "",
                                preview: ""
                            };
                            break
                        }
                        mw.AddDataToStore(RowID, data);
                        mw.ChangeRowList.push(RowID)
                    }
                    if (all[4] != "0" && parseInt(all[4]) > mw.refid) {
                        mw.refid = parseInt(all[4])
                    }
                    mw.RenderData()
                }
            })
        },
        GetOneInstrument: function(InsCode) {
            $.ajax({
                url: "tsev2/data/MarketWatchPlus.aspx",
                cache: true,
                data: {
                    i: InsCode
                },
                dataType: "html",
                success: function(data) {
                    var all = data.split("@");
                    var col = all[0].split(",");
                    var RowID = col[0];
                    mw.AddNewRowToStore(RowID, {
                        inscode: col[0],
                        iid: col[1],
                        l18: col[2],
                        l30: col[3],
                        py: col[14],
                        bvol: col[16],
                        visitcount: col[17],
                        flow: col[18],
                        cs: col[19],
                        tmax: col[20],
                        tmin: col[21],
                        z: col[22],
                        zo1: "",
                        zd1: "",
                        pd1: "",
                        po1: "",
                        qd1: "",
                        qo1: "",
                        _zo1: "",
                        _zd1: "",
                        _pd1: "",
                        _po1: "",
                        _qd1: "",
                        _qo1: "",
                        zo2: "",
                        zd2: "",
                        pd2: "",
                        po2: "",
                        qd2: "",
                        qo2: "",
                        _zo2: "",
                        _zd2: "",
                        _pd2: "",
                        _po2: "",
                        _qd2: "",
                        _qo2: "",
                        zo3: "",
                        zd3: "",
                        pd3: "",
                        po3: "",
                        qd3: "",
                        qo3: "",
                        _zo3: "",
                        _zd3: "",
                        _pd3: "",
                        _po3: "",
                        _qd3: "",
                        _qo3: "",
                        render: "",
                        preview: ""
                    });
                    mw.AddDataToStore(RowID, {
                        heven: col[4],
                        pf: col[5],
                        pc: col[6],
                        pcc: "" + parseInt(col[6]) - parseInt(col[13]),
                        pcp: "" + AdvRound(100 * (parseInt(col[6]) - parseInt(col[13])) / parseInt(col[13]), 2),
                        pl: col[7],
                        plc: "" + parseInt(col[7]) - parseInt(col[13]),
                        plp: "" + AdvRound(100 * (parseInt(col[7]) - parseInt(col[13])) / parseInt(col[13]), 2),
                        tno: col[8],
                        tvol: col[9],
                        tval: col[10],
                        pmin: col[11],
                        pmax: col[12],
                        eps: col[14],
                        pe: col[14] == "" ? "" : AdvRound(parseInt(col[6]) / parseInt(col[14]), 2),
                        render: "",
                        preview: ""
                    });
                    var BestLimit = all[1].split(";");
                    for (ipos = 0; ipos < BestLimit.length; ipos++) {
                        var col = BestLimit[ipos].split(",");
                        var RowID = col[0];
                        var data;
                        switch (col[1]) {
                        case "1":
                            data = {
                                zo1: col[2],
                                zd1: col[3],
                                pd1: col[4],
                                po1: col[5],
                                qd1: col[6],
                                qo1: col[7]
                            };
                            break;
                        case "2":
                            data = {
                                zo2: col[2],
                                zd2: col[3],
                                pd2: col[4],
                                po2: col[5],
                                qd2: col[6],
                                qo2: col[7]
                            };
                            break;
                        case "3":
                            data = {
                                zo3: col[2],
                                zd3: col[3],
                                pd3: col[4],
                                po3: col[5],
                                qd3: col[6],
                                qo3: col[7]
                            };
                            break
                        }
                        mw.AddDataToStore(RowID, data)
                    }
                    mw.ChangeRowList.push(RowID);
                    mw.RenderData()
                }
            })
        },
        LoadClientTypeTimer: null,
        LoadClientType: function() {
            if (mw.Settings.LoadClientType == 0) {
                return
            }
            window.clearTimeout(mw.LoadClientTypeTimer);
            $.ajax({
                url: "tsev2/data/ClientTypeAll.aspx",
                cache: true,
                dataType: "text",
                success: function(data) {
                    if (data.length == 0) {
                        return
                    }
                    var rows = data.split(";");
                    var cols;
                    var jd;
                    for (var qpos = 0; qpos < rows.length; qpos++) {
                        cols = rows[qpos].split(",");
                        jd = {
                            Buy_CountI: parseInt(cols[1], 10),
                            Buy_CountN: parseInt(cols[2], 10),
                            Buy_I_Volume: parseInt(cols[3], 10),
                            Buy_N_Volume: parseInt(cols[4], 10),
                            Sell_CountI: parseInt(cols[5], 10),
                            Sell_CountN: parseInt(cols[6], 10),
                            Sell_I_Volume: parseInt(cols[7], 10),
                            Sell_N_Volume: parseInt(cols[8], 10)
                        };
                        mw.ClientType[cols[0]] = jd
                    }
                    mw.LoadClientTypeTimer = window.setTimeout(mw.LoadClientType, 60000)
                }
            })
        },
        LoadInstStat: function() {
            if (mw.Settings.LoadInstStat == 0) {
                return
            }
            $.ajax({
                url: "tsev2/data/InstValue.aspx",
                data: {
                    t: "a"
                },
                cache: true,
                dataType: "text",
                success: function(data) {
                    var InsCode = "";
                    var rows = data.split(";");
                    var cols;
                    var jd;
                    for (var qpos = 0; qpos < rows.length; qpos++) {
                        cols = rows[qpos].split(",");
                        if (cols.length == 3) {
                            InsCode = cols[0];
                            if (typeof mw.InstStat[InsCode] == "undefined") {
                                mw.InstStat[InsCode] = {}
                            }
                            mw.InstStat[InsCode][cols[1]] = parseFloat(cols[2])
                        } else {
                            if (typeof mw.InstStat[InsCode] == "undefined") {
                                mw.InstStat[InsCode] = {}
                            }
                            mw.InstStat[InsCode][cols[0]] = parseFloat(cols[1])
                        }
                    }
                }
            })
        },
        LoadInstHistory: function() {
            if (mw.Settings.LoadInstHistory == 0) {
                return
            }
            $.ajax({
                url: MembersSite() + "/tsev2/data/ClosingPriceAll.aspx",
                cache: true,
                dataType: "text",
                success: function(data) {
                    var InsCode = "";
                    var rows = data.split(";");
                    var cols;
                    var jd;
                    var offset;
                    var days;
                    for (var qpos = 0; qpos < rows.length; qpos++) {
                        cols = rows[qpos].split(",");
                        if (cols.length == 11) {
                            InsCode = cols[0];
                            offset = 1
                        } else {
                            offset = 0
                        }
                        days = parseInt(cols[offset], 10);
                        if (typeof mw.InstHistory[InsCode] == "undefined") {
                            mw.InstHistory[InsCode] = []
                        }
                        mw.InstHistory[InsCode][days] = {
                            PClosing: parseFloat(cols[offset + 1]),
                            PDrCotVal: parseFloat(cols[offset + 2]),
                            ZTotTran: parseFloat(cols[offset + 3]),
                            QTotTran5J: parseFloat(cols[offset + 4]),
                            QTotCap: parseFloat(cols[offset + 5]),
                            PriceMin: parseFloat(cols[offset + 6]),
                            PriceMax: parseFloat(cols[offset + 7]),
                            PriceYesterday: parseFloat(cols[offset + 8]),
                            PriceFirst: parseFloat(cols[offset + 9])
                        }
                    }
                }
            })
        },
        RemoveAllData: function() {
            document.getElementById("main").innerHTML = "";
            mw.FirstTime = true;
            for (var key in mw.AllRows) {
                if (mw.AllRows.hasOwnProperty(key)) {
                    mw.AllRows[key].render = ""
                }
            }
        },
        RenderOne: function(row) {
            var rowHTML = MWTemplates[mw.Settings.ActiveTemplate].row;
            rowHTML = rowHTML.replace(/{i}/g, row.inscode);
            rowHTML = rowHTML.replace("{l18}", row.l18);
            rowHTML = rowHTML.replace("{l30}", row.l30);
            rowHTML = rowHTML.replace("{heven}", row.heven);
            rowHTML = rowHTML.replace("{pf}", addCommas(row.pf));
            rowHTML = rowHTML.replace("{pc}", addCommas(row.pc));
            rowHTML = rowHTML.replace("{pcc}", colorNum(row.pcc));
            rowHTML = rowHTML.replace("{pcp}", colorNum(row.pcp));
            rowHTML = rowHTML.replace("{pl}", addCommas(row.pl));
            rowHTML = rowHTML.replace("{plc}", colorNum(row.plc));
            rowHTML = rowHTML.replace("{plp}", colorNum(row.plp));
            rowHTML = rowHTML.replace("{tno}", addCommas(row.tno));
            rowHTML = rowHTML.replace("{tvol}", mw.ShowVol(row.tvol, row.bvol));
            rowHTML = rowHTML.replace("{tval}", mw.Settings.BigNumberSymbol == 1 ? bigNumber(row.tval) : addCommas(row.tval));
            rowHTML = rowHTML.replace("{pmin}", addCommas(row.pmin));
            rowHTML = rowHTML.replace("{pmax}", addCommas(row.pmax));
            rowHTML = rowHTML.replace("{py}", addCommas(row.py));
            rowHTML = rowHTML.replace("{eps}", row.eps == "" ? "-" : row.eps);
            rowHTML = rowHTML.replace("{pe}", row.pe == "" ? "-" : row.pe);
            rowHTML = rowHTML.replace("{bvol}", addCommas(row.bvol));
            rowHTML = rowHTML.replace("{zo1}", addCommas(row.zo1));
            rowHTML = rowHTML.replace("{zd1}", addCommas(row.zd1));
            rowHTML = rowHTML.replace("{pd1}", addCommas(row.pd1));
            rowHTML = rowHTML.replace("{po1}", addCommas(row.po1));
            rowHTML = rowHTML.replace("{qd1}", mw.Settings.BigNumberSymbol == 1 ? bigNumber(row.qd1) : addCommas(row.qd1));
            rowHTML = rowHTML.replace("{qo1}", mw.Settings.BigNumberSymbol == 1 ? bigNumber(row.qo1) : addCommas(row.qo1));
            rowHTML = rowHTML.replace("{zo2}", addCommas(row.zo2));
            rowHTML = rowHTML.replace("{zd2}", addCommas(row.zd2));
            rowHTML = rowHTML.replace("{pd2}", addCommas(row.pd2));
            rowHTML = rowHTML.replace("{po2}", addCommas(row.po2));
            rowHTML = rowHTML.replace("{qd2}", mw.Settings.BigNumberSymbol == 1 ? bigNumber(row.qd2) : addCommas(row.qd2));
            rowHTML = rowHTML.replace("{qo2}", mw.Settings.BigNumberSymbol == 1 ? bigNumber(row.qo2) : addCommas(row.qo2));
            rowHTML = rowHTML.replace("{zo3}", addCommas(row.zo3));
            rowHTML = rowHTML.replace("{zd3}", addCommas(row.zd3));
            rowHTML = rowHTML.replace("{pd3}", addCommas(row.pd3));
            rowHTML = rowHTML.replace("{po3}", addCommas(row.po3));
            rowHTML = rowHTML.replace("{qd3}", mw.Settings.BigNumberSymbol == 1 ? bigNumber(row.qd3) : addCommas(row.qd3));
            rowHTML = rowHTML.replace("{qo3}", mw.Settings.BigNumberSymbol == 1 ? bigNumber(row.qo3) : addCommas(row.qo3));
            rowHTML = rowHTML.replace("{cfield0}", row.cfield0);
            rowHTML = rowHTML.replace("{cfield1}", row.cfield1);
            rowHTML = rowHTML.replace("{cfield2}", row.cfield2);
            if (mw.Settings.ColorChangeEnable == 1) {
                rowHTML = rowHTML.replace("{_heven}", row._heven);
                rowHTML = rowHTML.replace("{_pc}", row._pc);
                rowHTML = rowHTML.replace("{_pcc}", row._pcc);
                rowHTML = rowHTML.replace("{_pcp}", row._pcp);
                rowHTML = rowHTML.replace("{_pl}", row._pl);
                rowHTML = rowHTML.replace("{_plc}", row._plc);
                rowHTML = rowHTML.replace("{_plp}", row._plp);
                rowHTML = rowHTML.replace("{_tno}", row._tno);
                rowHTML = rowHTML.replace("{_tvol}", row._tvol);
                rowHTML = rowHTML.replace("{_tval}", row._tval);
                rowHTML = rowHTML.replace("{_pmin}", row._pmin);
                rowHTML = rowHTML.replace("{_pmax}", row._pmax);
                rowHTML = rowHTML.replace("{_eps}", row._eps);
                rowHTML = rowHTML.replace("{_pe}", row._pe);
                rowHTML = rowHTML.replace("{_zo1}", row._zo1);
                rowHTML = rowHTML.replace("{_zd1}", row._zd1);
                rowHTML = rowHTML.replace("{_pd1}", row._pd1);
                rowHTML = rowHTML.replace("{_po1}", row._po1);
                rowHTML = rowHTML.replace("{_qd1}", row._qd1);
                rowHTML = rowHTML.replace("{_qo1}", row._qo1)
            }
            return rowHTML
        },
        RenderData: function() {
            var flow;
            var BodyHTML = [];
            var RenderNo = 0;
            var yval = "";
            for (var key in mw.AllRows) {
                if (!mw.AllRows.hasOwnProperty(key)) {
                    continue
                }
                var row = mw.AllRows[key];
                if (mw.preOpen == false && mw.Settings.ViewMode == 1 && row.tno == "0") {
                    continue
                }
                if (mw.Settings.ViewMode == 2 && mw.BasketInsts.indexOf(row.inscode) == -1) {
                    continue
                }
                if (mw.Settings.ViewMode == 3 && mw.Settings.SectorNo != row.cs) {
                    continue
                }
                flow = row.flow;
                if (mw.Settings.Market == 1 && (flow != "1" && flow != "3")) {
                    continue
                }
                if (mw.Settings.Market == 2 && (flow == "1" || flow == "3")) {
                    continue
                }
                if (mw.Settings.ShowHousingFacilities == 0) {
                    if (row.l18.indexOf("تسه") == 0 || row.l18.indexOf("تملي") == 0) {
                        continue
                    }
                }
                yval = row.yval;
                if (mw.Settings.ShowSaham == 0 && (yval == "300" || yval == "303" || yval == "313") && row.l18.indexOf("تسه") != 0) {
                    continue
                }
                if (mw.Settings.ShowPayeFarabourse == 0 && (yval == "309")) {
                    continue
                }
                if (mw.Settings.ShowHaghTaghaddom == 0 && (yval == "400" || yval == "403" || yval == "404")) {
                    continue
                }
                if (mw.Settings.ShowOraghMosharekat == 0 && (yval == "306" || yval == "301" || yval == "706" || yval == "208")) {
                    continue
                }
                if (mw.Settings.ShowAti == 0 && (yval == "263")) {
                    continue
                }
                if (mw.Settings.ShowSandoogh == 0 && (yval == "305" || yval == "380")) {
                    continue
                }
                if (mw.Settings.ShowEkhtiarForoush == 0 && (yval == "600" || yval == "602" || yval == "605" || yval == "311" || yval == "312")) {
                    continue
                }
                if (mw.Settings.ShowKala == 0 && (yval == "308" || yval == "701")) {
                    continue
                }
                if (mw.FilterCode.length != 0) {
                    var FilterResult;
                    try {
                        if (typeof mw.ClientType[row.inscode] == "undefined") {
                            mw.ClientType[row.inscode] = {
                                Buy_CountI: 0,
                                Buy_CountN: 0,
                                Buy_I_Volume: 0,
                                Buy_N_Volume: 0,
                                Sell_CountI: 0,
                                Sell_CountN: 0,
                                Sell_I_Volume: 0,
                                Sell_N_Volume: 0
                            }
                        }
                        FilterResult = eval(mw.FilterCode)
                    } catch (e) {
                        FilterResult = false
                    }
                    if (!FilterResult) {
                        if (document.getElementById(row.inscode) != null) {
                            if (!mw.FirstTime && mw.NotificationPermission) {
                                mw.showNotification(row.l18, "خروج از فیلتر " + mw.Settings.Filters[mw.Settings.FilterNo].FilterName)
                            }
                            $(document.getElementById(row.inscode)).remove().empty()
                        }
                    } else {
                        if (row.render.length == 0) {
                            var RowHTML = mw.RenderOne(row);
                            row.render = "-";
                            if (document.getElementById(row.inscode) != null) {
                                document.getElementById(row.inscode).innerHTML = RowHTML
                            } else {
                                if (mw.Settings.GroupBySector == 1 && document.getElementById("S" + row.cs) == null) {
                                    $(document.getElementById("main")).append('<div class="secSep" id="S' + row.cs + '">' + mw.SectorName(row.cs) + "</div>")
                                }
                                $(document.getElementById("main")).append('<div class="{c}" id="' + row.inscode + '" onclick="mw.SelectRow(this,\'' + row.inscode + "')\" ondblclick=\"ManageBaskets('" + row.inscode + '\')" style="' + MWTemplates[mw.Settings.ActiveTemplate].rowStyle + '">' + RowHTML + "</div>");
                                if (!mw.FirstTime && mw.NotificationPermission) {
                                    mw.showNotification(row.l18, "ورود به فیلتر " + mw.Settings.Filters[mw.Settings.FilterNo].FilterName)
                                }
                            }
                        }
                    }
                } else {
                    if (row.render.length == 0) {
                        var RowHTML = mw.RenderOne(row);
                        row.render = "-";
                        if (document.getElementById(row.inscode) != null) {
                            document.getElementById(row.inscode).innerHTML = RowHTML
                        } else {
                            if (mw.Settings.GroupBySector == 1 && document.getElementById("S" + row.cs) == null) {
                                $(document.getElementById("main")).append('<div class="secSep" id="S' + row.cs + '">' + mw.SectorName(row.cs) + "</div>")
                            }
                            $(document.getElementById("main")).append('<div class="{c}" id="' + row.inscode + '" onclick="mw.SelectRow(this,\'' + row.inscode + "')\" ondblclick=\"ManageBaskets('" + row.inscode + '\')" style="' + MWTemplates[mw.Settings.ActiveTemplate].rowStyle + '">' + RowHTML + "</div>")
                        }
                    }
                }
            }
            var t1 = mw.Settings.UpdateSpeed;
            if (mw.FirstTime || t1 >= 8000 || (t1 >= 4000 && mw.RoundNo % 2 == 0) || mw.RoundNo == 2) {
                mw.SortData()
            }
            mw.RenderPreview();
            mw.ResetChangeInStore();
            mw.ClearChangeStatus();
            if (typeof timer1 != "undefined") {
                window.clearTimeout(timer1)
            }
            timer1 = window.setTimeout("mw.UpdateMarketWatch()", parseInt(t1));
            if (mw.userFullName) {
                $("#userFullName").html("نام کاربر :" + mw.userFullName);
                $("#userLink").html("خروج").attr("href", "javascript:mw.logOutUser()")
            } else {
                $("#userFullName").html("");
                $("#userLink").attr("href", "https://members.tsetmc.com/UserLoginnew.aspx?" + window.location.href).html("ورود")
            }
            mw.FirstTime = false
        },
        showNotification: function(title, body) {
            var notification = new Notification(title,{
                dir: "auto",
                lang: "",
                body: body,
                tag: "",
                icon: ""
            })
        },
        AutoScroll: function(status) {
            if (!status) {
                if (typeof AutoScrollTimer != "undefined") {
                    window.clearTimeout(AutoScrollTimer)
                }
            } else {
                var MainDiv = document.getElementById("main");
                if (MainDiv.scrollTop >= MainDiv.scrollHeight - MainDiv.clientHeight) {
                    MainDiv.scrollTop = 0
                } else {
                    MainDiv.scrollTop += MainDiv.clientHeight * 0.9
                }
                AutoScrollTimer = window.setTimeout("mw.AutoScroll(true)", 7000)
            }
        },
        ClearChangeStatus: function() {
            var CleanNo = mw.RoundNo + 2;
            if (CleanNo > 8) {
                CleanNo = CleanNo - 8
            }
            $(".ch" + CleanNo).removeClass("ch" + CleanNo)
        }
    };
    return MarketWatchPlus
}
;;