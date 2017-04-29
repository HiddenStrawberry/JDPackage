# coding=utf-8
#差3个参数和一个pwd的处理 有没有大佬能搞出来
import PyV8
import requests
import re
import base64
from JDPackage.rk import *
import random
class mjdLogin:
    def __init__(self, username, pwd):
        rdname = str(random.randint(1000000, 10000000))
        self.rc = RClient('#', '#')  #ruokuai login
        self.username=username
        self.pwd=pwd
        self.url = 'http://plogin.m.jd.com/user/login.action?appid=100&kpkey=&returnurl=https%3A%2F%2Fp.m.jd.com%2Fcart%2Fcart.action%3Fsid%3D55b4b7248c6b7ca957a97a4bd32d6f0a'
        self.session=requests.session()
        self.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36 115Browser/8.0.0',
                      'Accept': 'application / json',
                      'Cookie':'Cookie: abtest=20170228211138104_31; guid=6433233c81bef27af5c14a5bc4c2f4697474b06d86bdabc10fda151371c15d8d; mt_xid=V2_52007VwMXUFRbW10bQB1sUm8CFFcPCwFGHk1LDxliBhFQQQhXDhtVSVkMNwoaW15eBglLeRpdBWEfE1dBWFJLHkkSWABsARtiX2hSahdJEF8DZwYbVlReUlgZShpaBWMzEldbXw%3D%3D; jdAddrId=; jdAddrName=; m_uuid_new=BCD37AFFEA2F15B81125F84F8FA12FD1; user-key=764d61c5-fec3-4a36-a77d-49ec9c6d313d; downloadAppPlugIn_downCloseDate_m_index_shield=1493054478115_86400000; s_key=AAFY_jqdADDu-jNlm8vkNVVRP8IJSr_95D9rdeD0KAMRnOhYVGYVZNACo9r7oStMo-FEcXWg714; s_pin=jd_yftmsye93940; rememberMe=""; logincheck=""; unpl=V2_ZzNtbUJTExN8D05TeUoPB2JUFVVKAxNHc19PAysaCQRlUBAOclRCFXMUR1FnGlgUZwAZXEJcRhdFCEdkcxFUDGcKGm1HVUoddzh2V3spXARXAxdfS1RKEnEBQmRLHmw1soqjhMbRlKfkOEFRfRtVA2cAIlxyVnNeGwkLVH4bVQZuBBZURmdCJXY%3d; cn=0; lsid=hm4j7ozjdcpckh4r7h5s2xs3m12ggiby; ipLoc-djd=1-72-2799-0; ipLocation=%u5317%u4EAC; areaId=1; USER_FLAG_CHECK=88cdc3f388eb4286ab784b6cb0c5466e; autoOpenApp_downCloseDate_auto=1493135190091_1800000; regionAddress=8%2C560%2C569%2C; commonAddress=; __jdv=122270672|iosapp|t_335139774|appshare|Qqfriends|1493135415094; warehistory="12163054,11345039,12020612,12004800,10873775,10873776,11157785,11970902,11097352,11775072,"; sid=55b4b7248c6b7ca957a97a4bd32d6f0a; returnurl="https://p.m.jd.com/cart/cart.action?sid=55b4b7248c6b7ca957a97a4bd32d6f0a"; TrackID=1_hV_wIpzpJhf8tSWomgEiP8KBTLXAG0Oos7Cx-pReFbzS8Wl7x-wGZ5daVKQVUna8WxSET8yetsYSVPrYXZyLnIRG43Ls61bF392vMfKMQs; pinId=FfPbtfY-QJ_HjtdcPvAX-w; pin=18842484750_p; unick=EGE-36727066; _tp=%2Fc1PP1BuP2EIevl8u0TdHg%3D%3D; _pst=18842484750_p; ceshi3.com=201; 3AB9D23F7A4B3C9B=7H7IWLLE6VH2LJFWNYO3ORSASUSWLL2EAJFIEPDOBTMPS6JIVJD3FFYMTLWSCOO2ROZ7USBVEHIWUTMN4UCZGT5FUM; thor=48F8A6BDB23C29D8D9AC565BF85839AEC68ADEDA080D9C4C63CA6D97808ED5F33B47FDFB37C1E27FDAA789F788CBDFF72C8AF57C3EEBF13A8D39A8AA3322065A6E7C449AA7FE77649D22002F8FC13987865C54CDDD25B0C9FD83947972AF5080DB4E172D7CCA4D8C6FECFC0872E2942FE67E570CD4AE25D4F4D3BF71E933DE9218A8050ED66FC9157CB6CD4B471EE495; shshshfpa=bbcf93bd-2314-652c-f87e-bec0c34d22cb-1493140403; __jda=122270672.1438286585.1486822411.1493134468.1493135189.46; __jdb=122270672.9.1438286585|46.1493135189; __jdc=122270672; shshshfpb=0147c511af31133375d1918f5a4f349e49f5d88f0030bece758ff83ac5; __jdu=1438286585; whwswswws=vT7uItGSS1gK8v+pOKga2KiAIEiKTw%2FwGw1T6stGTN5RoWB5Bw02RQ%3D%3D; mba_muid=1438286585; mba_sid=14931403849169354662104292752.1'
                      }
        self.html = self.session.get(self.url,headers=self.headers,verify=False).text
        self.str_rsaString = re.findall('str_rsaString = \'(.*?)\'', self.html, re.S)[0]
        self.str_kenString = re.findall('str_kenString = \'(.*?)\'', self.html, re.S)[0]
        authimgurl='http://plogin.m.jd.com'+re.findall('<img id="imgCode" src="(.*?)"',self.html,re.S)[0]
        ir = self.session.get(authimgurl,headers=self.headers,verify=False)
        fp = open('C:\\temp\\' + rdname + '.png', 'wb')
        fp.write(ir.content)
        fp.close()
        im = open('C:\\temp\\' + rdname + '.png', 'rb').read()
        self.authcode = self.rc.rk_create(im, 3040)['Result']
        self.datax = {'username': username,
                 'pwd': self.get_pwd(self.pwd), #PWD有问题
                 'remember': 'true',
                 's_token': self.str_kenString,
                 'dat': self.get_dat(self.username, self.pwd),
                 'wlfstk_datk': self.get_dat(self.username, self.pwd),
                 'authcode': self.authcode,
                 'risk_jd[eid]':'????', #3个risk参数有问题
                 'risk_jd[fp]':'????',
                 'risk_jd[token]':'????'
                 }
        print self.datax
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36 115Browser/8.0.0','Referer': self.url}
        print requests.post('http://plogin.m.jd.com/cgi-bin/m/domlogin', data=self.datax, headers=self.headers).text

    def get_eid(self):
        a = """var _JdEid = "",
	_eidFlag = !1,
	risk_jd_local_fingerprint = "";
(function(n, r, u) {
	"undefined" !== typeof module && module.exports ? module.exports = u() : "function" === typeof define && define.amd ? define(u) : r[n] = u()
})("JdJrTdRiskFinger", this, function() {
	function n(a) {
		if (null == a || void 0 == a || "" == a) return "undefined";
		var b;
		if (null == a || void 0 == a || "" == a) b = "";
		else {
			b = [];
			for (var c = 0; c < 8 * a.length; c += 8) b[c >> 5] |= (a.charCodeAt(c / 8) & 255) << c % 32
		}
		a = 8 * a.length;
		b[a >> 5] |= 128 << a % 32;
		b[(a + 64 >>> 9 << 4) + 14] = a;
		a = 1732584193;
		for (var c = -271733879, e = -1732584194, k = 271733878, f = 0; f < b.length; f += 16) {
			var g = a,
				h = c,
				l = e,
				q = k;
			a = u(a, c, e, k, b[f + 0], 7, -680876936);
			k = u(k, a, c, e, b[f + 1], 12, -389564586);
			e = u(e, k, a, c, b[f + 2], 17, 606105819);
			c = u(c, e, k, a, b[f + 3], 22, -1044525330);
			a = u(a, c, e, k, b[f + 4], 7, -176418897);
			k = u(k, a, c, e, b[f + 5], 12, 1200080426);
			e = u(e, k, a, c, b[f + 6], 17, -1473231341);
			c = u(c, e, k, a, b[f + 7], 22, -45705983);
			a = u(a, c, e, k, b[f + 8], 7, 1770035416);
			k = u(k, a, c, e, b[f + 9], 12, -1958414417);
			e = u(e, k, a, c, b[f + 10], 17, -42063);
			c = u(c, e, k, a, b[f + 11], 22, -1990404162);
			a = u(a, c, e, k, b[f + 12], 7, 1804603682);
			k = u(k, a, c, e, b[f + 13], 12, -40341101);
			e = u(e, k, a, c, b[f + 14], 17, -1502002290);
			c = u(c, e, k, a, b[f + 15], 22, 1236535329);
			a = v(a, c, e, k, b[f + 1], 5, -165796510);
			k = v(k, a, c, e, b[f + 6], 9, -1069501632);
			e = v(e, k, a, c, b[f + 11], 14, 643717713);
			c = v(c, e, k, a, b[f + 0], 20, -373897302);
			a = v(a, c, e, k, b[f + 5], 5, -701558691);
			k = v(k, a, c, e, b[f + 10], 9, 38016083);
			e = v(e, k, a, c, b[f + 15], 14, -660478335);
			c = v(c, e, k, a, b[f + 4], 20, -405537848);
			a = v(a, c, e, k, b[f + 9], 5, 568446438);
			k = v(k, a, c, e, b[f + 14], 9, -1019803690);
			e = v(e, k, a, c, b[f + 3], 14, -187363961);
			c = v(c, e, k, a, b[f + 8], 20, 1163531501);
			a = v(a, c, e, k, b[f + 13], 5, -1444681467);
			k = v(k, a, c, e, b[f + 2], 9, -51403784);
			e = v(e, k, a, c, b[f + 7], 14, 1735328473);
			c = v(c, e, k, a, b[f + 12], 20, -1926607734);
			a = r(c ^ e ^ k, a, c, b[f + 5], 4, -378558);
			k = r(a ^ c ^ e, k, a, b[f + 8], 11, -2022574463);
			e = r(k ^ a ^ c, e, k, b[f + 11], 16, 1839030562);
			c = r(e ^ k ^ a, c, e, b[f + 14], 23, -35309556);
			a = r(c ^ e ^ k, a, c, b[f + 1], 4, -1530992060);
			k = r(a ^ c ^ e, k, a, b[f + 4], 11, 1272893353);
			e = r(k ^ a ^ c, e, k, b[f + 7], 16, -155497632);
			c = r(e ^ k ^ a, c, e, b[f + 10], 23, -1094730640);
			a = r(c ^ e ^ k, a, c, b[f + 13], 4, 681279174);
			k = r(a ^ c ^ e, k, a, b[f + 0], 11, -358537222);
			e = r(k ^ a ^ c, e, k, b[f + 3], 16, -722521979);
			c = r(e ^ k ^ a, c, e, b[f + 6], 23, 76029189);
			a = r(c ^ e ^ k, a, c, b[f + 9], 4, -640364487);
			k = r(a ^ c ^ e, k, a, b[f + 12], 11, -421815835);
			e = r(k ^ a ^ c, e, k, b[f + 15], 16, 530742520);
			c = r(e ^ k ^ a, c, e, b[f + 2], 23, -995338651);
			a = t(a, c, e, k, b[f + 0], 6, -198630844);
			k = t(k, a, c, e, b[f + 7], 10, 1126891415);
			e = t(e, k, a, c, b[f + 14], 15, -1416354905);
			c = t(c, e, k, a, b[f + 5], 21, -57434055);
			a = t(a, c, e, k, b[f + 12], 6, 1700485571);
			k = t(k, a, c, e, b[f + 3], 10, -1894986606);
			e = t(e, k, a, c, b[f + 10], 15, -1051523);
			c = t(c, e, k, a, b[f + 1], 21, -2054922799);
			a = t(a, c, e, k, b[f + 8], 6, 1873313359);
			k = t(k, a, c, e, b[f + 15], 10, -30611744);
			e = t(e, k, a, c, b[f + 6], 15, -1560198380);
			c = t(c, e, k, a, b[f + 13], 21, 1309151649);
			a = t(a, c, e, k, b[f + 4], 6, -145523070);
			k = t(k, a, c, e, b[f + 11], 10, -1120210379);
			e = t(e, k, a, c, b[f + 2], 15, 718787259);
			c = t(c, e, k, a, b[f + 9], 21, -343485551);
			a = x(a, g);
			c = x(c, h);
			e = x(e, l);
			k = x(k, q)
		}
		b = [a, c, e, k];
		a = "";
		for (c = 0; c < 4 * b.length; c++) a += "0123456789abcdef".charAt(b[c >> 2] >> c % 4 * 8 + 4 & 15) + "0123456789abcdef".charAt(b[c >> 2] >> c % 4 * 8 & 15);
		return a
	}
	function r(a, b, c, e, f, g) {
		a = x(x(b, a), x(e, g));
		return x(a << f | a >>> 32 - f, c)
	}
	function u(a, b, c, e, f, g, h) {
		return r(b & c | ~b & e, a, b, f, g, h)
	}
	function v(a, b, c, e, f, g, h) {
		return r(b & e | c & ~e, a, b, f, g, h)
	}
	function t(a, b, c, e, f, g, h) {
		return r(c ^ (b | ~e), a, b, f, g, h)
	}
	function x(a, b) {
		var c = (a & 65535) + (b & 65535);
		return (a >> 16) + (b >> 16) + (c >> 16) << 16 | c & 65535
	}
	var f = "unknown",
		m = "unknown";
	try {
		-1 != e.indexOf("win") && -1 != e.indexOf("95") && (f = "windows", m = "95"), -1 != e.indexOf("win") && -1 != e.indexOf("98") && (f = "windows", m = "98"), -1 != e.indexOf("win 9x") && -1 != e.indexOf("4.90") && (f = "windows", m = "me"), -1 != e.indexOf("win") && -1 != e.indexOf("nt 5.0") && (f = "windows", m = "2000"), -1 != e.indexOf("win") && -1 != e.indexOf("nt") && (f = "windows", m = "NT"), -1 != e.indexOf("win") && -1 != e.indexOf("nt 5.1") && (f = "windows", m = "xp"), -1 != e.indexOf("win") && -1 != e.indexOf("32") && (f = "windows", m = "32"), -1 != e.indexOf("win") && -1 != e.indexOf("nt 5.1") && (f = "windows", m = "7"), -1 != e.indexOf("win") && -1 != e.indexOf("6.0") && (f = "windows", m = "8"), -1 == e.indexOf("win") || -1 == e.indexOf("nt 6.0") && -1 == e.indexOf("nt 6.1") || (f = "windows", m = "9"), -1 != e.indexOf("win") && -1 != e.indexOf("nt 6.2") && (f = "windows", m = "10"), -1 != e.indexOf("linux") && (f = "linux"), -1 != e.indexOf("unix") && (f = "unix"), -1 != e.indexOf("sun") && -1 != e.indexOf("os") && (f = "sun os"), -1 != e.indexOf("ibm") && -1 != e.indexOf("os") && (f = "ibm os/2"), -1 != e.indexOf("mac") && -1 != e.indexOf("pc") && (f = "mac"), -1 != e.indexOf("aix") && (f = "aix"), -1 != e.indexOf("powerpc") && (f = "powerPC"), -1 != e.indexOf("hpux") && (f = "hpux"), -1 != e.indexOf("netbsd") && (f = "NetBSD"), -1 != e.indexOf("bsd") && (f = "BSD"), -1 != e.indexOf("osf1") && (f = "OSF1"), -1 != e.indexOf("irix") && (f = "IRIX", m = ""), -1 != e.indexOf("freebsd") && (f = "FreeBSD"), -1 != e.indexOf("symbianos") && (f = "SymbianOS", m = e.substring(e.indexOf("SymbianOS/") + 10, 3))
	} catch (a) {}
	var q = "unknown",
		w = "unknown";
	try {
		-1 != e.indexOf("msie") && (q = "ie", w = e.substring(e.indexOf("msie ") + 5), w.indexOf(";") && (w = w.substring(0, w.indexOf(";")))); - 1 != e.indexOf("firefox") && (q = "Firefox", w = e.substring(e.indexOf("firefox/") + 8)); - 1 != e.indexOf("opera") && (q = "Opera", w = e.substring(e.indexOf("opera/") + 6, 4)); - 1 != e.indexOf("safari") && (q = "safari", w = e.substring(e.indexOf("safari/") + 7)); - 1 != e.indexOf("chrome") && (q = "chrome", w = e.substring(e.indexOf("chrome/") + 7), w.indexOf(" ") && (w = w.substring(0, w.indexOf(" ")))); - 1 != e.indexOf("navigator") && (q = "navigator", w = e.substring(e.indexOf("navigator/") + 10)); - 1 != e.indexOf("applewebkit") && (q = "applewebkit_chrome", w = e.substring(e.indexOf("applewebkit/") + 12), w.indexOf(" ") && (w = w.substring(0, w.indexOf(" ")))); - 1 != e.indexOf("sogoumobilebrowser") && (q = "");
		if (-1 != e.indexOf("ucbrowser") || -1 != e.indexOf("ucweb")) q = "";
		if (-1 != e.indexOf("qqbrowser") || -1 != e.indexOf("tencenttraveler")) q = ""; - 1 != e.indexOf("metasr") && (q = ""); - 1 != e.indexOf("360se") && (q = ""); - 1 != e.indexOf("the world") && (q = ""); - 1 != e.indexOf("maxthon") && (q = "")
	} catch (a) {}
	e = function(a) {
		this.options = this.extend(a, {});
		this.nativeForEach = Array.prototype.forEach;
		this.nativeMap = Array.prototype.map
	};
	e.prototype = {
		extend: function(a, b) {
			if (null == a) return b;
			for (var c in a) null != a[c] && b[c] !== a[c] && (b[c] = a[c]);
			return b
		},
		getData: function() {
			return g
		},
		get: function(a) {
			var b = 1 * w,
				c = [];
			"ie" == q && 7 <= b ? (c.push(h), c.push(l), g = g + ",'userAgent':'" + n(h) + "','language':'" + l + "'", this.browserRedirect(h)) : (c = this.userAgentKey(c), c = this.languageKey(c));
			c.push(q);
			c.push(w);
			c.push(f);
			c.push(m);
			g = g + ",'os':'" + f + "','osVersion':'" + m + "','browser':'" + q + "','browserVersion':'" + w + "'";
			c = this.colorDepthKey(c);
			c = this.screenResolutionKey(c);
			c = this.timezoneOffsetKey(c);
			c = this.sessionStorageKey(c);
			c = this.localStorageKey(c);
			c = this.indexedDbKey(c);
			c = this.addBehaviorKey(c);
			c = this.openDatabaseKey(c);
			c = this.cpuClassKey(c);
			c = this.platformKey(c);
			c = this.doNotTrackKey(c);
			c = this.pluginsKey(c);
			c = this.canvasKey(c);
			c = this.webglKey(c);
			b = this.x64hash128(c.join("~~~"), 31);
			return a(b)
		},
		
		replaceAll: function(a, b, c) {
			for (; 0 <= a.indexOf(b);) a = a.replace(b, c);
			return a
		},
		browserRedirect: function(a) {
			var b = a.toLowerCase();
			a = "ipad" == b.match(/ipad/i);
			var c = "iphone os" == b.match(/iphone os/i),
				e = "midp" == b.match(/midp/i),
				f = "rv:1.2.3.4" == b.match(/rv:1.2.3.4/i),
				h = "ucweb" == b.match(/ucweb/i),
				l = "android" == b.match(/android/i),
				q = "windows ce" == b.match(/windows ce/i),
				b = "windows mobile" == b.match(/windows mobile/i);
			g = a || c || e || f || h || l || q || b ? g + ",'origin':'mobile'" : g + ",'origin':'pc'"
		},
		
		colorDepthKey: function(a) {
			this.options.excludeColorDepth || (a.push(screen.colorDepth), g = g + ",'colorDepth':'" + screen.colorDepth + "'");
			return a
		},
		screenResolutionKey: function(a) {
			if (!this.options.excludeScreenResolution) {
				var b = this.getScreenResolution();
				"undefined" !== typeof b && (a.push(b.join("x")), g = g + ",'screenResolution':'" + b.join("x") + "'")
			}
			return a
		},
		getScreenResolution: function() {
			return this.options.detectScreenOrientation ? screen.height > screen.width ? [screen.height, screen.width] : [screen.width, screen.height] : [screen.height, screen.width]
		},
		timezoneOffsetKey: function(a) {
			this.options.excludeTimezoneOffset || (a.push((new Date).getTimezoneOffset()), g = g + ",'timezoneOffset':'" + (new Date).getTimezoneOffset() / 60 + "'");
			return a
		},
		sessionStorageKey: function(a) {
			!this.options.excludeSessionStorage && this.hasSessionStorage() && (a.push("sessionStorageKey"), g += ",'sessionStorage':true");
			return a
		},
		localStorageKey: function(a) {
			!this.options.excludeSessionStorage && this.hasLocalStorage() && (a.push("localStorageKey"), g += ",'localStorage':true");
			return a
		},
		indexedDbKey: function(a) {
			!this.options.excludeIndexedDB && this.hasIndexedDB() && (a.push("indexedDbKey"), g += ",'indexedDb':true");
			return a
		},
		addBehaviorKey: function(a) {
			document.body && !this.options.excludeAddBehavior && document.body.addBehavior ? (a.push("addBehaviorKey"), g += ",'addBehavior':true") : g += ",'addBehavior':false";
			return a
		},
		openDatabaseKey: function(a) {
			!this.options.excludeOpenDatabase && window.openDatabase ? (a.push("openDatabase"), g += ",'openDatabase':true") : g += ",'openDatabase':false";
			return a
		},
		
		doNotTrackKey: function(a) {
			this.options.excludeDoNotTrack || (a.push(this.getDoNotTrack()), g = g + ",'track':'" + this.getDoNotTrack() + "'");
			return a
		},
		canvasKey: function(a) {
			!this.options.excludeCanvas && this.isCanvasSupported() && (a.push(this.getCanvasFp()), g = g + ",'canvas':'" + n(this.getCanvasFp()) + "'");
			return a
		},
		webglKey: function(a) {
			!this.options.excludeWebGL && this.isCanvasSupported() && (a.push(this.getWebglFp()), g = g + ",'webglFp':'" + n(this.getWebglFp()) + "'");
			return a
		},
		pluginsKey: function(a) {
			this.isIE() ? (a.push(this.getIEPluginsString()), g = g + ",'plugins':'" + n(this.getIEPluginsString()) + "'") : (a.push(this.getRegularPluginsString()), g = g + ",'plugins':'" + n(this.getRegularPluginsString()) + "'");
			return a
		},
		
		getIEPluginsString: function() {
			return window.ActiveXObject ? this.map("AcroPDF.PDF;Adodb.Stream;AgControl.AgControl;DevalVRXCtrl.DevalVRXCtrl.1;MacromediaFlashPaper.MacromediaFlashPaper;Msxml2.DOMDocument;Msxml2.XMLHTTP;PDF.PdfCtrl;QuickTime.QuickTime;QuickTimeCheckObject.QuickTimeCheck.1;RealPlayer;RealPlayer.RealPlayer(tm) ActiveX Control (32-bit);RealVideo.RealVideo(tm) ActiveX Control (32-bit);Scripting.Dictionary;SWCtl.SWCtl;Shell.UIHelper;ShockwaveFlash.ShockwaveFlash;Skype.Detection;TDCCtl.TDCCtl;WMPlayer.OCX;rmocx.RealPlayer G2 Control;rmocx.RealPlayer G2 Control.1".split(";"), function(a) {
				try {
					return new ActiveXObject(a), a
				} catch (b) {
					return null
				}
			}).join(";") : ""
		},
		hasSessionStorage: function() {
			try {
				return !!window.sessionStorage
			} catch (a) {
				return !0
			}
		},
		hasLocalStorage: function() {
			try {
				return !!window.localStorage
			} catch (a) {
				return !0
			}
		},
		hasIndexedDB: function() {
			return !!window.indexedDB
		},
		
		getWebglFp: function() {
			
				a = a.toLowerCase();
			if ((0 < a.indexOf("jdjr-app") || 0 <= a.indexOf("jdapp")) && (0 < a.indexOf("iphone") || 0 < a.indexOf("ipad"))) return null;
			var b, a = function(a) {
					b.clearColor(0, 0, 0, 1);
					b.enable(b.DEPTH_TEST);
					b.depthFunc(b.LEQUAL);
					b.clear(b.COLOR_BUFFER_BIT | b.DEPTH_BUFFER_BIT);
					return "[" + a[0] + ", " + a[1] + "]"
				};
			b = this.getWebglCanvas();
			if (!b) return null;
			var c = [],
				e = b.createBuffer();
			b.bindBuffer(b.ARRAY_BUFFER, e);
			var f = new Float32Array([-.2, -.9, 0, .4, -.26, 0, 0, .732134444, 0]);
			b.bufferData(b.ARRAY_BUFFER, f, b.STATIC_DRAW);
			e.itemSize = 3;
			e.numItems = 3;
			var f = b.createProgram(),
				g = b.createShader(b.VERTEX_SHADER);
			b.shaderSource(g, "attribute vec2 attrVertex;varying vec2 varyinTexCoordinate;uniform vec2 uniformOffset;void main(){varyinTexCoordinate=attrVertex+uniformOffset;gl_Position=vec4(attrVertex,0,1);}");
			b.compileShader(g);
			var h = b.createShader(b.FRAGMENT_SHADER);
			b.shaderSource(h, "precision mediump float;varying vec2 varyinTexCoordinate;void main() {gl_FragColor=vec4(varyinTexCoordinate,0,1);}");
			b.compileShader(h);
			b.attachShader(f, g);
			b.attachShader(f, h);
			b.linkProgram(f);
			b.useProgram(f);
			f.vertexPosAttrib = b.getAttribLocation(f, "attrVertex");
			f.offsetUniform = b.getUniformLocation(f, "uniformOffset");
			b.enableVertexAttribArray(f.vertexPosArray);
			b.vertexAttribPointer(f.vertexPosAttrib, e.itemSize, b.FLOAT, !1, 0, 0);
			b.uniform2f(f.offsetUniform, 1, 1);
			b.drawArrays(b.TRIANGLE_STRIP, 0, e.numItems);
			null != b.canvas && c.push(b.canvas.toDataURL());
			c.push("extensions:" + b.getSupportedExtensions().join(";"));
			c.push("webgl aliased line width range:" + a(b.getParameter(b.ALIASED_LINE_WIDTH_RANGE)));
			c.push("webgl aliased point size range:" + a(b.getParameter(b.ALIASED_POINT_SIZE_RANGE)));
			c.push("webgl alpha bits:" + b.getParameter(b.ALPHA_BITS));
			c.push("webgl antialiasing:" + (b.getContextAttributes().antialias ? "yes" : "no"));
			c.push("webgl blue bits:" + b.getParameter(b.BLUE_BITS));
			c.push("webgl depth bits:" + b.getParameter(b.DEPTH_BITS));
			c.push("webgl green bits:" + b.getParameter(b.GREEN_BITS));
			c.push("webgl max anisotropy:" +
			function(a) {
				var b, c = a.getExtension("EXT_texture_filter_anisotropic") || a.getExtension("WEBKIT_EXT_texture_filter_anisotropic") || a.getExtension("MOZ_EXT_texture_filter_anisotropic");
				return c ? (b = a.getParameter(c.MAX_TEXTURE_MAX_ANISOTROPY_EXT), 0 === b && (b = 2), b) : null
			}(b));
			c.push("webgl max combined texture image units:" + b.getParameter(b.MAX_COMBINED_TEXTURE_IMAGE_UNITS));
			c.push("webgl max cube map texture size:" + b.getParameter(b.MAX_CUBE_MAP_TEXTURE_SIZE));
			c.push("webgl max fragment uniform vectors:" + b.getParameter(b.MAX_FRAGMENT_UNIFORM_VECTORS));
			c.push("webgl max render buffer size:" + b.getParameter(b.MAX_RENDERBUFFER_SIZE));
			c.push("webgl max texture image units:" + b.getParameter(b.MAX_TEXTURE_IMAGE_UNITS));
			c.push("webgl max texture size:" + b.getParameter(b.MAX_TEXTURE_SIZE));
			c.push("webgl max varying vectors:" + b.getParameter(b.MAX_VARYING_VECTORS));
			c.push("webgl max vertex attribs:" + b.getParameter(b.MAX_VERTEX_ATTRIBS));
			c.push("webgl max vertex texture image units:" + b.getParameter(b.MAX_VERTEX_TEXTURE_IMAGE_UNITS));
			c.push("webgl max vertex uniform vectors:" + b.getParameter(b.MAX_VERTEX_UNIFORM_VECTORS));
			c.push("webgl max viewport dims:" + a(b.getParameter(b.MAX_VIEWPORT_DIMS)));
			c.push("webgl red bits:" + b.getParameter(b.RED_BITS));
			c.push("webgl renderer:" + b.getParameter(b.RENDERER));
			c.push("webgl shading language version:" + b.getParameter(b.SHADING_LANGUAGE_VERSION));
			c.push("webgl stencil bits:" + b.getParameter(b.STENCIL_BITS));
			c.push("webgl vendor:" + b.getParameter(b.VENDOR));
			c.push("webgl version:" + b.getParameter(b.VERSION));
			return c.join("")
		},
		isCanvasSupported: function() {
			var a = document.createElement("canvas");
			return !(!a.getContext || !a.getContext("2d"))
		},
		
		getWebglCanvas: function() {
			var a = document.createElement("canvas"),
				b = null;
			try {
				
					c = c.toLowerCase();
				(0 < c.indexOf("jdjr-app") || 0 <= c.indexOf("jdapp")) && (0 < c.indexOf("iphone") || 0 < c.indexOf("ipad")) || (b = a.getContext("webgl") || a.getContext("experimental-webgl"))
			} catch (y) {}
			b || (b = null);
			return b
		},
		each: function(a, b, c) {
			if (null !== a) if (this.nativeForEach && a.forEach === this.nativeForEach) a.forEach(b, c);
			else if (a.length === +a.length) for (var e = 0, f = a.length; e < f && b.call(c, a[e], e, a) !== {}; e++);
			else for (e in a) if (a.hasOwnProperty(e) && b.call(c, a[e], e, a) === {}) break
		},
		map: function(a, b, c) {
			var e = [];
			if (null == a) return e;
			if (this.nativeMap && a.map === this.nativeMap) return a.map(b, c);
			this.each(a, function(a, f, g) {
				e[e.length] = b.call(c, a, f, g)
			});
			return e
		},
		x64Add: function(a, b) {
			a = [a[0] >>> 16, a[0] & 65535, a[1] >>> 16, a[1] & 65535];
			b = [b[0] >>> 16, b[0] & 65535, b[1] >>> 16, b[1] & 65535];
			var c = [0, 0, 0, 0];
			c[3] += a[3] + b[3];
			c[2] += c[3] >>> 16;
			c[3] &= 65535;
			c[2] += a[2] + b[2];
			c[1] += c[2] >>> 16;
			c[2] &= 65535;
			c[1] += a[1] + b[1];
			c[0] += c[1] >>> 16;
			c[1] &= 65535;
			c[0] += a[0] + b[0];
			c[0] &= 65535;
			return [c[0] << 16 | c[1], c[2] << 16 | c[3]]
		},
		x64Multiply: function(a, b) {
			a = [a[0] >>> 16, a[0] & 65535, a[1] >>> 16, a[1] & 65535];
			b = [b[0] >>> 16, b[0] & 65535, b[1] >>> 16, b[1] & 65535];
			var c = [0, 0, 0, 0];
			c[3] += a[3] * b[3];
			c[2] += c[3] >>> 16;
			c[3] &= 65535;
			c[2] += a[2] * b[3];
			c[1] += c[2] >>> 16;
			c[2] &= 65535;
			c[2] += a[3] * b[2];
			c[1] += c[2] >>> 16;
			c[2] &= 65535;
			c[1] += a[1] * b[3];
			c[0] += c[1] >>> 16;
			c[1] &= 65535;
			c[1] += a[2] * b[2];
			c[0] += c[1] >>> 16;
			c[1] &= 65535;
			c[1] += a[3] * b[1];
			c[0] += c[1] >>> 16;
			c[1] &= 65535;
			c[0] += a[0] * b[3] + a[1] * b[2] + a[2] * b[1] + a[3] * b[0];
			c[0] &= 65535;
			return [c[0] << 16 | c[1], c[2] << 16 | c[3]]
		},
		x64Rotl: function(a, b) {
			b %= 64;
			if (32 === b) return [a[1], a[0]];
			if (32 > b) return [a[0] << b | a[1] >>> 32 - b, a[1] << b | a[0] >>> 32 - b];
			b -= 32;
			return [a[1] << b | a[0] >>> 32 - b, a[0] << b | a[1] >>> 32 - b]
		},
		x64LeftShift: function(a, b) {
			b %= 64;
			return 0 === b ? a : 32 > b ? [a[0] << b | a[1] >>> 32 - b, a[1] << b] : [a[1] << b - 32, 0]
		},
		x64Xor: function(a, b) {
			return [a[0] ^ b[0], a[1] ^ b[1]]
		},
		x64Fmix: function(a) {
			a = this.x64Xor(a, [0, a[0] >>> 1]);
			a = this.x64Multiply(a, [4283543511, 3981806797]);
			a = this.x64Xor(a, [0, a[0] >>> 1]);
			a = this.x64Multiply(a, [3301882366, 444984403]);
			return a = this.x64Xor(a, [0, a[0] >>> 1])
		},
		x64hash128: function(a, b) {
			a = a || "";
			b = b || 0;
			var c = a.length % 16,
				e = a.length - c,
				f = [0, b];
			b = [0, b];
			for (var g, h, l = [2277735313, 289559509], q = [1291169091, 658871167], m = 0; m < e; m += 16) g = [a.charCodeAt(m + 4) & 255 | (a.charCodeAt(m + 5) & 255) << 8 | (a.charCodeAt(m + 6) & 255) << 16 | (a.charCodeAt(m + 7) & 255) << 24, a.charCodeAt(m) & 255 | (a.charCodeAt(m + 1) & 255) << 8 | (a.charCodeAt(m + 2) & 255) << 16 | (a.charCodeAt(m + 3) & 255) << 24], h = [a.charCodeAt(m + 12) & 255 | (a.charCodeAt(m + 13) & 255) << 8 | (a.charCodeAt(m + 14) & 255) << 16 | (a.charCodeAt(m + 15) & 255) << 24, a.charCodeAt(m + 8) & 255 | (a.charCodeAt(m + 9) & 255) << 8 | (a.charCodeAt(m + 10) & 255) << 16 | (a.charCodeAt(m + 11) & 255) << 24], g = this.x64Multiply(g, l), g = this.x64Rotl(g, 31), g = this.x64Multiply(g, q), f = this.x64Xor(f, g), f = this.x64Rotl(f, 27), f = this.x64Add(f, b), f = this.x64Add(this.x64Multiply(f, [0, 5]), [0, 1390208809]), h = this.x64Multiply(h, q), h = this.x64Rotl(h, 33), h = this.x64Multiply(h, l), b = this.x64Xor(b, h), b = this.x64Rotl(b, 31), b = this.x64Add(b, f), b = this.x64Add(this.x64Multiply(b, [0, 5]), [0, 944331445]);
			g = [0, 0];
			h = [0, 0];
			switch (c) {
			case 15:
				h = this.x64Xor(h, this.x64LeftShift([0, a.charCodeAt(m + 14)], 48));
			case 14:
				h = this.x64Xor(h, this.x64LeftShift([0, a.charCodeAt(m + 13)], 40));
			case 13:
				h = this.x64Xor(h, this.x64LeftShift([0, a.charCodeAt(m + 12)], 32));
			case 12:
				h = this.x64Xor(h, this.x64LeftShift([0, a.charCodeAt(m + 11)], 24));
			case 11:
				h = this.x64Xor(h, this.x64LeftShift([0, a.charCodeAt(m + 10)], 16));
			case 10:
				h = this.x64Xor(h, this.x64LeftShift([0, a.charCodeAt(m + 9)], 8));
			case 9:
				h = this.x64Xor(h, [0, a.charCodeAt(m + 8)]), h = this.x64Multiply(h, q), h = this.x64Rotl(h, 33), h = this.x64Multiply(h, l), b = this.x64Xor(b, h);
			case 8:
				g = this.x64Xor(g, this.x64LeftShift([0, a.charCodeAt(m + 7)], 56));
			case 7:
				g = this.x64Xor(g, this.x64LeftShift([0, a.charCodeAt(m + 6)], 48));
			case 6:
				g = this.x64Xor(g, this.x64LeftShift([0, a.charCodeAt(m + 5)], 40));
			case 5:
				g = this.x64Xor(g, this.x64LeftShift([0, a.charCodeAt(m + 4)], 32));
			case 4:
				g = this.x64Xor(g, this.x64LeftShift([0, a.charCodeAt(m + 3)], 24));
			case 3:
				g = this.x64Xor(g, this.x64LeftShift([0, a.charCodeAt(m + 2)], 16));
			case 2:
				g = this.x64Xor(g, this.x64LeftShift([0, a.charCodeAt(m + 1)], 8));
			case 1:
				g = this.x64Xor(g, [0, a.charCodeAt(m)]), g = this.x64Multiply(g, l), g = this.x64Rotl(g, 31), g = this.x64Multiply(g, q), f = this.x64Xor(f, g)
			}
			f = this.x64Xor(f, [0, a.length]);
			b = this.x64Xor(b, [0, a.length]);
			f = this.x64Add(f, b);
			b = this.x64Add(b, f);
			f = this.x64Fmix(f);
			b = this.x64Fmix(b);
			f = this.x64Add(f, b);
			b = this.x64Add(b, f);
			return ("00000000" + (f[0] >>> 0).toString(16)).slice(-8) + ("00000000" + (f[1] >>> 0).toString(16)).slice(-8) + ("00000000" + (b[0] >>> 0).toString(16)).slice(-8) + ("00000000" + (b[1] >>> 0).toString(16)).slice(-8)
		}
	};
	return e
});

	_JdJrTdRiskDomainName = "payrisk.jd.com",
	_CurrentPageUrl = function() {
		
		0 < n.indexOf("?") && (n = n.substring(0, n.indexOf("?")));
		return n = n.substring(_CurrentPageProtocol.length)
	}(),
	td_collect = new function() {
		function n() {
			var g = window.webkitRTCPeerConnection || window.mozRTCPeerConnection || window.RTCPeerConnection;
			if (g) {
				var h = function(f) {
						var g = /([0-9]{1,3}(\.[0-9]{1,3}){3})/;
						try {
							var h = g.exec(f)[1];
							void 0 === e[h] && v.push(h);
							e[h] = !0
						} catch (w) {}
					},
					l, e = {};
				try {
					l = new g({
						iceServers: [{
							url: "stun:stun.services.mozilla.com"
						}]
					})
				} catch (f) {}
				try {
					void 0 === l && (l = new g({
						iceServers: []
					}))
				} catch (f) {}
				if (l || window.mozRTCPeerConnection) try {
					l.createDataChannel("chat", {
						reliable: !1
					})
				} catch (f) {}
				l && (l.onicecandidate = function(e) {
					e.candidate && h(e.candidate.candidate)
				}, l.createOffer(function(e) {
					l.setLocalDescription(e, function() {}, function() {})
				}, function() {}), setTimeout(function() {
					try {
						l.localDescription.sdp.split("\\n").forEach(function(e) {
							0 === e.indexOf("a=candidate:") && h(e)
						})
					} catch (f) {}
				}, 800))
			}
		}
		function r() {
			function g(f) {
				var g = {};
				e.style.fontFamily = f;
				
				g.height = e.offsetHeight;
				g.width = e.offsetWidth;
				
				
				return g
			}
			var h = ["monospace", "sans-serif", "serif"],
				l = [],
				e = document.createElement("span");
			e.style.fontSize = "72px";
			e.style.visibility = "hidden";
			e.innerHTML = "mmmmmmmmmmlli";
			for (var f = 0; f < h.length; f++) l[f] = g(h[f]);
			this.checkSupportFont = function(e) {
				for (var f = 0; f < l.length; f++) {
					var m = g(e + "," + h[f]),
						a = l[f];
					if (m.height !== a.height || m.width !== a.width) return !0
				}
				return !1
			}
		}
		function u(g) {
			var h = {};
			h.name = g.name;
			h.filename = g.filename.toLowerCase();
			h.description = g.description;
			void 0 !== g.version && (h.version = g.version);
			h.mimeTypes = [];
			for (var l = 0; l < g.length; l++) {
				var e = g[l],
					f = {};
				f.description = e.description;
				f.suffixes = e.suffixes;
				f.type = e.type;
				h.mimeTypes.push(f)
			}
			return h
		}
		this.obtainLocal = function() {
			var g = {};
			try {
				var h = document.cookie.replace(/(?:(?:^|.*;\s*)3AB9D23F7A4B3C9B\s*\=\s*([^;]*).*$)|^.*$/, "$1");
				0 !== h.length && (g.cookie = h)
			} catch (f) {}
			try {
				window.localStorage && null !== window.localStorage && 0 !== window.localStorage.length && (g.localStorage = window.localStorage.getItem("3AB9D23F7A4B3C9B"))
			} catch (f) {}
			try {
				window.sessionStorage && null !== window.sessionStorage && (g.sessionStorage = window.sessionStorage["3AB9D23F7A4B3C9B"])
			} catch (f) {}
			try {
				p.globalStorage && (g.globalStorage = window.globalStorage[".localdomain"]["3AB9D23F7A4B3C9B"])
			} catch (f) {}
			try {
				d && "function" == typeof d.load && "function" == typeof d.getAttribute && (d.load("payegis_user_data"), g.userData = d.getAttribute("3AB9D23F7A4B3C9B"))
			} catch (f) {}
			try {
				E.indexedDbId && (g.indexedDb = E.indexedDbId)
			} catch (f) {}
			try {
				E.webDbId && (g.webDb = E.webDbId)
			} catch (f) {}
			try {
				for (var l in g) if (32 < g[l].length) {
					_JdEid = g[l];
					_eidFlag = !0;
					break
				}
			} catch (f) {}
			if ("undefined" === typeof _JdEid || 0 >= _JdEid.length) _JdEid = this.db("3AB9D23F7A4B3C9B");
			if ("undefined" === typeof _JdEid || 0 >= _JdEid.length) {
				var e;
				_JdEid = (e = document.cookie.match(/(^| )3AB9D23F7A4B3C9B=([^;]*)(;|$)/)) ? e[2] : ""
			}
			if ("undefined" === typeof _JdEid || 0 >= _JdEid.length) _eidFlag = !0;
			return _JdEid
		};
		var v = [],
			t = "Abadi MT Condensed Light;Adobe Fangsong Std;Adobe Hebrew;Adobe Ming Std;Agency FB;Arab;Arabic Typesetting;Arial Black;Batang;Bauhaus 93;Bell MT;Bitstream Vera Serif;Bodoni MT;Bookman Old Style;Braggadocio;Broadway;Calibri;Californian FB;Castellar;Casual;Centaur;Century Gothic;Chalkduster;Colonna MT;Copperplate Gothic Light;DejaVu LGC Sans Mono;Desdemona;DFKai-SB;Dotum;Engravers MT;Eras Bold ITC;Eurostile;FangSong;Forte;Franklin Gothic Heavy;French Script MT;Gabriola;Gigi;Gisha;Goudy Old Style;Gulim;GungSeo;Haettenschweiler;Harrington;Hiragino Sans GB;Impact;Informal Roman;KacstOne;Kino MT;Kozuka Gothic Pr6N;Lohit Gujarati;Loma;Lucida Bright;Lucida Fax;Magneto;Malgun Gothic;Matura MT Script Capitals;Menlo;MingLiU-ExtB;MoolBoran;MS PMincho;MS Reference Sans Serif;News Gothic MT;Niagara Solid;Nyala;Palace Script MT;Papyrus;Perpetua;Playbill;PMingLiU;Rachana;Rockwell;Sawasdee;Script MT Bold;Segoe Print;Showcard Gothic;SimHei;Snap ITC;TlwgMono;Tw Cen MT Condensed Extra Bold;Ubuntu;Umpush;Univers;Utopia;Vladimir Script;Wide Latin".split(";"),
			x = "4game;AdblockPlugin;AdobeExManCCDetect;AdobeExManDetect;Alawar NPAPI utils;Aliedit Plug-In;Alipay Security Control 3;AliSSOLogin plugin;AmazonMP3DownloaderPlugin;AOL Media Playback Plugin;AppUp;ArchiCAD;AVG SiteSafety plugin;Babylon ToolBar;Battlelog Game Launcher;BitCometAgent;Bitdefender QuickScan;BlueStacks Install Detector;CatalinaGroup Update;Citrix ICA Client;Citrix online plug-in;Citrix Receiver Plug-in;Coowon Update;DealPlyLive Update;Default Browser Helper;DivX Browser Plug-In;DivX Plus Web Player;DivX VOD Helper Plug-in;doubleTwist Web Plugin;Downloaders plugin;downloadUpdater;eMusicPlugin DLM6;ESN Launch Mozilla Plugin;ESN Sonar API;Exif Everywhere;Facebook Plugin;File Downloader Plug-in;FileLab plugin;FlyOrDie Games Plugin;Folx 3 Browser Plugin;FUZEShare;GDL Object Web Plug-in 16.00;GFACE Plugin;Ginger;Gnome Shell Integration;Google Earth Plugin;Google Earth Plug-in;Google Gears 0.5.33.0;Google Talk Effects Plugin;Google Update;Harmony Firefox Plugin;Harmony Plug-In;Heroes & Generals live;HPDetect;Html5 location provider;IE Tab plugin;iGetterScriptablePlugin;iMesh plugin;Kaspersky Password Manager;LastPass;LogMeIn Plugin 1.0.0.935;LogMeIn Plugin 1.0.0.961;Ma-Config.com plugin;Microsoft Office 2013;MinibarPlugin;Native Client;Nitro PDF Plug-In;Nokia Suite Enabler Plugin;Norton Identity Safe;npAPI Plugin;NPLastPass;NPPlayerShell;npTongbuAddin;NyxLauncher;Octoshape Streaming Services;Online Storage plug-in;Orbit Downloader;Pando Web Plugin;Parom.TV player plugin;PDF integrado do WebKit;PDF-XChange Viewer;PhotoCenterPlugin1.1.2.2;Picasa;PlayOn Plug-in;QQ2013 Firefox Plugin;QQDownload Plugin;QQMiniDL Plugin;QQMusic;RealDownloader Plugin;Roblox Launcher Plugin;RockMelt Update;Safer Update;SafeSearch;Scripting.Dictionary;SefClient Plugin;Shell.UIHelper;Silverlight Plug-In;Simple Pass;Skype Web Plugin;SumatraPDF Browser Plugin;Symantec PKI Client;Tencent FTN plug-in;Thunder DapCtrl NPAPI Plugin;TorchHelper;Unity Player;Uplay PC;VDownloader;Veetle TV Core;VLC Multimedia Plugin;Web Components;WebKit-integrierte PDF;WEBZEN Browser Extension;Wolfram Mathematica;WordCaptureX;WPI Detector 1.4;Yandex Media Plugin;Yandex PDF Viewer;YouTube Plug-in;zako".split(";");
		this.toJson = "object" === typeof JSON && JSON.stringify;
		this.init = function() {
			n();
			"function" !== typeof this.toJson && (this.toJson = function(g) {
				var h;
				h = typeof g;
				if ("undefined" === h || null === g) return "null";
				if ("number" === h || "boolean" === h) return g + "";
				if ("object" === h && g && g.constructor === Array) {
					h = [];
					for (var l = 0; g.length > l; l++) h.push(this.toJson(g[l]));
					return "[" + (h + "") + "]"
				}
				if ("object" === h) {
					h = [];
					for (l in g) g.hasOwnProperty(l) && h.push('"' + l + '":' + this.toJson(g[l]));
					return "{" + (h + "") + "}"
				}
			})
		};
		this.minHash = function(g) {
			var h, l, e, f = g.length & 3,
				m = g.length - f;
			h = void 0;
			for (e = 0; e < m;) l = g.charCodeAt(e) & 255 | (g.charCodeAt(++e) & 255) << 8 | (g.charCodeAt(++e) & 255) << 16 | (g.charCodeAt(++e) & 255) << 24, ++e, l = 3432918353 * (l & 65535) + ((3432918353 * (l >>> 16) & 65535) << 16) & 4294967295, l = l << 15 | l >>> 17, l = 461845907 * (l & 65535) + ((461845907 * (l >>> 16) & 65535) << 16) & 4294967295, h ^= l, h = h << 13 | h >>> 19, h = 5 * (h & 65535) + ((5 * (h >>> 16) & 65535) << 16) & 4294967295, h = (h & 65535) + 27492 + (((h >>> 16) + 58964 & 65535) << 16);
			l = 0;
			switch (f) {
			case 3:
				l ^= (g.charCodeAt(e + 2) & 255) << 16;
			case 2:
				l ^= (g.charCodeAt(e + 1) & 255) << 8;
			case 1:
				l ^= g.charCodeAt(e) & 255, l = 3432918353 * (l & 65535) + ((3432918353 * (l >>> 16) & 65535) << 16) & 4294967295, l = l << 15 | l >>> 17, h ^= 461845907 * (l & 65535) + ((461845907 * (l >>> 16) & 65535) << 16) & 4294967295
			}
			h ^= g.length;
			h ^= h >>> 16;
			h = 2246822507 * (h & 65535) + ((2246822507 * (h >>> 16) & 65535) << 16) & 4294967295;
			h ^= h >>> 13;
			h = 3266489909 * (h & 65535) + ((3266489909 * (h >>> 16) & 65535) << 16) & 4294967295;
			return (h ^ h >>> 16) >>> 0
		};
		this.db = function(g, h) {
			try {
				if (window.openDatabase) {
					var l = window.openDatabase("sqlite_jdtdstorage", "", "jdtdstorage", 1048576);
					void 0 !== h ? l.transaction(function(e) {
						e.executeSql("CREATE TABLE IF NOT EXISTS cache(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, value TEXT NOT NULL, UNIQUE (name))", [], function(e, g) {}, function(e, g) {});
						e.executeSql("INSERT OR REPLACE INTO cache(name, value) VALUES(?, ?)", [g, h], function(e, g) {}, function(e, g) {})
					}) : l.transaction(function(e) {
						e.executeSql("SELECT value FROM cache WHERE name=?", [g], function(e, g) {
							self._ec.dbData = 1 <= g.rows.length ? g.rows.item(0).value : ""
						}, function(e, g) {})
					})
				}
			} catch (e) {}
		};
		this.tdencrypt = function(g) {
			g = this.toJson(g);
			g = encodeURIComponent(g);
			var h = "",
				l, e, f, m, q, n, a = 0;
			do l = g.charCodeAt(a++), e = g.charCodeAt(a++), f = g.charCodeAt(a++), m = l >> 2, l = (l & 3) << 4 | e >> 4, q = (e & 15) << 2 | f >> 6, n = f & 63, isNaN(e) ? q = n = 64 : isNaN(f) && (n = 64), h = h + "23IL<N01c7KvwZO56RSTAfghiFyzWJqVabGH4PQdopUrsCuX*xeBjkltDEmn89.-".charAt(m) + "23IL<N01c7KvwZO56RSTAfghiFyzWJqVabGH4PQdopUrsCuX*xeBjkltDEmn89.-".charAt(l) + "23IL<N01c7KvwZO56RSTAfghiFyzWJqVabGH4PQdopUrsCuX*xeBjkltDEmn89.-".charAt(q) + "23IL<N01c7KvwZO56RSTAfghiFyzWJqVabGH4PQdopUrsCuX*xeBjkltDEmn89.-".charAt(n);
			while (a < g.length);
			return h + "/"
		};
		this.collect = function() {
			var g = new Date;
			try {
				var h = document.createElement("div"),
					l = {},
					e = "ActiveBorder ActiveCaption AppWorkspace Background ButtonFace ButtonHighlight ButtonShadow ButtonText CaptionText GrayText Highlight HighlightText InactiveBorder InactiveCaption InactiveCaptionText InfoBackground InfoText Menu MenuText Scrollbar ThreeDDarkShadow ThreeDFace ThreeDHighlight ThreeDLightShadow ThreeDShadow Window WindowFrame WindowText".split(" ");
				if (window.getComputedStyle) for (var f = 0; f < e.length; f++) document.body.appendChild(h), h.style.color = e[f], l[e[f]] = window.getComputedStyle(h).getPropertyValue("color"), document.body.removeChild(h)
			} catch (A) {}
			var h = {
				ca: {},
				ts: {},
				m: {}
			},
				e = h.ca,
				m, q, f = 0;
			try {
				m = document.createElement("canvas"), q = m.getContext("2d")
			} catch (A) {}
			q && (q.fillStyle = "red", q.fillRect(30, 10, 200, 100), q.strokeStyle = "#1a3bc1", q.lineWidth = 6, q.lineCap = "round", q.arc(50, 50, 20, 0, Math.PI, !1), q.stroke(), q.fillStyle = "#42e1a2", q.font = "15.4px 'Arial'", q.textBaseline = "alphabetic", q.fillText("PR flacks quiz gym: TV DJ box when?", 15, 60), q.shadowOffsetX = 1, q.shadowOffsetY = 2, q.shadowColor = "white", q.fillStyle = "rgba(0, 0, 200, 0.5)", q.font = "60px 'Not a real font'", q.fillText("No", 40, 80), f = this.minHash(m.toDataURL()));
			e.tdHash = f;
			m = !1;
			if (f) {
				q = ["webgl", "experimental-webgl", "moz-webgl", "webkit-3d"];
				for (var n = [], a, f = 0; f < q.length; f++) try {
					var b = !1;
					(b = document.createElement("canvas").getContext(q[f], {
						stencil: !0
					})) && b && (a = b, n.push(q[f]))
				} catch (A) {}
				n.length && (m = {
					name: n,
					gl: a
				})
			}
			if (m) {
				f = m.gl;
				e.contextName = m.name.join();
				e.webglversion = f.getParameter(f.VERSION);
				e.shadingLV = f.getParameter(f.SHADING_LANGUAGE_VERSION);
				e.vendor = f.getParameter(f.VENDOR);
				e.renderer = f.getParameter(f.RENDERER);
				a = [];
				try {
					a = f.getSupportedExtensions(), e.extensions = a
				} catch (A) {}
			}
			h.ts.deviceTime = g.getTime();
			h.m.documentMode = document.documentMode;
			h.m.compatMode = document.compatMode;
			e = [];
			a = new r;
			for (f = 0; f < t.length; f++) m = t[f], a.checkSupportFont(m) && e.push(m);
			h.fo = e;
			var f = {},
				e = [],
				c;
			for (c in navigator)"object" != typeof navigator[c] && (f[c] = navigator[c]), e.push(c);
			f.enumerationOrder = e;
			f.javaEnabled = navigator.javaEnabled();
			try {
				f.taintEnabled = navigator.taintEnabled()
			} catch (A) {}
			h.n = f;
			var f = navigator.userAgent.toLowerCase(),
				y;
			if (c = f.match(/rv:([\d.]+)\) like gecko/)) y = c[1];
			if (c = f.match(/msie ([\d.]+)/)) y = c[1];
			c = [];
			if (y) for (y = "AcroPDF.PDF;Adodb.Stream;AgControl.AgControl;DevalVRXCtrl.DevalVRXCtrl.1;MacromediaFlashPaper.MacromediaFlashPaper;Msxml2.DOMDocument;Msxml2.XMLHTTP;PDF.PdfCtrl;QuickTime.QuickTime;QuickTimeCheckObject.QuickTimeCheck.1;RealPlayer;RealPlayer.RealPlayer(tm) ActiveX Control (32-bit);RealVideo.RealVideo(tm) ActiveX Control (32-bit);rmocx.RealPlayer G2 Control;Scripting.Dictionary;Shell.UIHelper;ShockwaveFlash.ShockwaveFlash;SWCtl.SWCtl;TDCCtl.TDCCtl;WMPlayer.OCX".split(";"), f = 0; f < y.length; f++) {
				var k = y[f];
				try {
					var z = new ActiveXObject(k),
						e = {};
					e.name = k;
					try {
						e.version = z.GetVariable("$version")
					} catch (A) {}
					try {
						e.version = z.GetVersions()
					} catch (A) {}
					e.version && 0 < e.version.length || (e.version = "");
					c.push(e)
				} catch (A) {}
			} else {
				y = navigator.plugins;
				e = {};
				for (f = 0; f < y.length; f++) k = y[f], e[k.name] = 1, c.push(u(k));
				for (f = 0; f < x.length; f++) z = x[f], e[z] || (k = y[z], k && c.push(u(k)))
			}
			y = "availHeight availWidth colorDepth bufferDepth deviceXDPI deviceYDPI height width logicalXDPI logicalYDPI pixelDepth updateInterval".split(" ");
			k = {};
			for (f = 0; y.length > f; f++) z = y[f], void 0 !== screen[z] && (k[z] = screen[z]);
			y = ["devicePixelRatio", "screenTop", "screenLeft"];
			e = {};
			for (f = 0; y.length > f; f++) z = y[f], void 0 !== window[z] && (e[z] = window[z]);
			h.p = c;
			h.w = e;
			h.s = k;
			h.sc = l;
			h.tz = g.getTimezoneOffset();
			h.lil = v.sort().join("|");
			h.wil = "";
			g = {};
			try {
				g.cookie = navigator.cookieEnabled, g.localStorage = !! window.localStorage, g.sessionStorage = !! window.sessionStorage, g.globalStorage = !! window.globalStorage, g.indexedDB = !! window.indexedDB
			} catch (A) {}
			h.ss = g;
			return this.tdencrypt(h)
		}
	};

function td_collect_exe() {
	var n = td_collect.collect(),
		r = "undefined" === typeof orderId ? "" : orderId,
		r = {
			pin: _jdJrTdCommonsObtainPin(),
			oid: r,
			p: "https:" == document.location.protocol ? "s" : "h",
			fp: risk_jd_local_fingerprint
		};
	try {
		r.o = _CurrentPageUrl
	} catch (u) {}
	0 >= _JdEid.length && (_JdEid = td_collect.obtainLocal(), 0 < _JdEid.length && (_eidFlag = !0));
	r.fc = _JdEid;
	r = td_collect.tdencrypt(r);
	jdJrTdsendCorsRequest(_CurrentPageProtocol + _JdJrTdRiskDomainName + "/fcf.html?a=" + r, "d=" + n, function(n) {
		if (32 < n.length) {
			var r = 0 < n.indexOf("jd_risk_");
			r || (_JdEid = n);
			_eidFlag = !0;
			var t = new Date;
			t.setFullYear(t.getFullYear() + 1E3);
			try {
				_jdJrTdRelationEidPin(n), r || td_collect.setCookie("3AB9D23F7A4B3C9B", n)
			} catch (x) {}
			try {
				window.localStorage && window.localStorage.setItem("3AB9D23F7A4B3C9B", n)
			} catch (x) {}
			try {
				window.sessionStorage && window.sessionStorage.setItem("3AB9D23F7A4B3C9B", n)
			} catch (x) {}
			try {
				window.globalStorage && window.globalStorage[".localdomain"].setItem("3AB9D23F7A4B3C9B", n)
			} catch (x) {}
			try {
				td_collect.db("3AB9D23F7A4B3C9B", _JdEid)
			} catch (x) {}
		}
	}, !1)
}(function() {
	(new JdJrTdRiskFinger).get(function(n) {
		risk_jd_local_fingerprint = n;
		if (0 >= _JdEid.length || !_eidFlag) _JdEid = td_collect.obtainLocal(), 0 >= _JdEid.length && (_eidFlag = !0)
	});
	td_collect.init();
	try {
		td_collect_exe()
	} catch (n) {}
})();

function jdJrTdsendCorsRequest(n, r, u, v) {
	try {
		var t;
		try {
			t = new window.XMLHttpRequest
		} catch (x) {}
		if (!t) try {
			t = new window.ActiveXObject("Microsoft.XMLHTTP")
		} catch (x) {}
		if (!t) try {
			t = new window.ActiveXObject("Msxml2.XMLHTTP")
		} catch (x) {}
		if (!t) try {
			t = new window.ActiveXObject("Msxml3.XMLHTTP")
		} catch (x) {}
		t.open("POST", n, !1);
		t.setRequestHeader("Content-Type", "application/x-www-form-urlencoded;charset=UTF-8");
		t.onreadystatechange = function() {
			4 === t.readyState && 200 === t.status && u && u(t.responseText)
		};
		t.send(r)
	} catch (x) {}
}
function getJdEid() {
	var n = {
		eid: _JdEid,
		fp: risk_jd_local_fingerprint,
		token: ""
	};
	try {
		n.token = jd_risk_token_id
	} catch (r) {}
	return n
}
function JdJrTdFingerDataStream(n, r, u) {
	if ("undefined" !== typeof n && 0 != n) if (void 0 === r && (r = 1), void 0 === u && (u = 15), 0 >= _JdEid.length && r < u) setTimeout(function() {
		JdJrTdFingerDataStream(n, r, u)
	}, 20 * r), r++;
	else {
		if ("undefined" !== typeof jd_risk_token_id && 0 < _JdEid.length && 0 < risk_jd_local_fingerprint.length) {
			var v = _jdJrTdCommonsObtainPin();
			0 < v.length && (v = {
				p: v,
				fp: risk_jd_local_fingerprint,
				e: _JdEid,
				ct: (new Date).getTime(),
				t: jd_risk_token_id,
				opt: n
			}, jdJrTdsendCorsRequest(_CurrentPageProtocol + _JdJrTdRiskDomainName + "/stream.html", "c=" + td_collect.tdencrypt(v)))
		}
	} else throw Error("sourceCode can not be null.");
}
function _jdJrTdRelationEidPin(n) {
	try {
		if (32 <= n.length) {
			var r = _jdJrTdCommonsObtainPin();
			if (0 < r.length) {
				n = {
					o: _CurrentPageUrl,
					p: r,
					e: n,
					f: risk_jd_local_fingerprint
				};
				try {
					n.bizId = _jdtdparam.bizId, n.pvId = _jdtdparam.pvId, n.uvId = _jdtdparam.uvId
				} catch (v) {}
				var u = td_collect.tdencrypt(n);
				jdJrTdsendCorsRequest(_CurrentPageProtocol + _JdJrTdRiskDomainName + "/r.html?v=" + Math.random(), "&d=" + u)
			}
		}
	} catch (v) {}
}
function _jdJrTdCommonsObtainPin() {
	var n = "";
	"string" === typeof pin ? n = pin : "object" === typeof pin && "string" === typeof jd_jr_td_risk_pin && (n = jd_jr_td_risk_pin);
	return n
};"""
        ctxt = PyV8.JSContext()
        ctxt.enter()
        ctxt.eval(a)
        func = ctxt.locals.getJdEid
        a = func()
        return a

    def get_pwd(self, pwd):
        a = '''
        function BarrettMu(i) {
	this.modulus = biCopy(i), this.k = biHighIndex(this.modulus) + 1;
	var t = new BigInt;
	t.digits[2 * this.k] = 1, this.mu = biDivide(t, this.modulus), this.bkplus1 = new BigInt, this.bkplus1.digits[this.k + 1] = 1, this.modulo = BarrettMu_modulo, this.multiplyMod = BarrettMu_multiplyMod, this.powMod = BarrettMu_powMod
}
function BarrettMu_modulo(i) {
	var t = biDivideByRadixPower(i, this.k - 1),
		r = biMultiply(t, this.mu),
		e = biDivideByRadixPower(r, this.k + 1),
		n = biModuloByRadixPower(i, this.k + 1),
		g = biMultiply(e, this.modulus),
		s = biModuloByRadixPower(g, this.k + 1),
		d = biSubtract(n, s);
	d.isNeg && (d = biAdd(d, this.bkplus1));
	for (var o = biCompare(d, this.modulus) >= 0; o;) d = biSubtract(d, this.modulus), o = biCompare(d, this.modulus) >= 0;
	return d
}
function BarrettMu_multiplyMod(i, t) {
	var r = biMultiply(i, t);
	return this.modulo(r)
}
function BarrettMu_powMod(i, t) {
	var r = new BigInt;
	r.digits[0] = 1;
	for (var e = i, n = t;;) {
		if (0 != (1 & n.digits[0]) && (r = this.multiplyMod(r, e)), n = biShiftRight(n, 1), 0 == n.digits[0] && 0 == biHighIndex(n)) break;
		e = this.multiplyMod(e, e)
	}
	return r
}
function setMaxDigits(i) {
	maxDigits = i, ZERO_ARRAY = new Array(maxDigits);
	for (var t = 0; t < ZERO_ARRAY.length; t++) ZERO_ARRAY[t] = 0;
	bigZero = new BigInt, bigOne = new BigInt, bigOne.digits[0] = 1
}
function BigInt(i) {
	"boolean" == typeof i && 1 == i ? this.digits = null : this.digits = ZERO_ARRAY.slice(0), this.isNeg = !1
}
function biFromDecimal(i) {
	for (var t, r = "-" == i.charAt(0), e = r ? 1 : 0; e < i.length && "0" == i.charAt(e);)++e;
	if (e == i.length) t = new BigInt;
	else {
		var n = i.length - e,
			g = n % dpl10;
		for (0 == g && (g = dpl10), t = biFromNumber(Number(i.substr(e, g))), e += g; e < i.length;) t = biAdd(biMultiply(t, lr10), biFromNumber(Number(i.substr(e, dpl10)))), e += dpl10;
		t.isNeg = r
	}
	return t
}
function biCopy(i) {
	var t = new BigInt((!0));
	return t.digits = i.digits.slice(0), t.isNeg = i.isNeg, t
}
function biFromNumber(i) {
	var t = new BigInt;
	t.isNeg = i < 0, i = Math.abs(i);
	for (var r = 0; i > 0;) t.digits[r++] = i & maxDigitVal, i >>= biRadixBits;
	return t
}
function reverseStr(i) {
	for (var t = "", r = i.length - 1; r > -1; --r) t += i.charAt(r);
	return t
}
function biToString(i, t) {
	var r = new BigInt;
	r.digits[0] = t;
	for (var e = biDivideModulo(i, r), n = hexatrigesimalToChar[e[1].digits[0]]; 1 == biCompare(e[0], bigZero);) e = biDivideModulo(e[0], r), digit = e[1].digits[0], n += hexatrigesimalToChar[e[1].digits[0]];
	return (i.isNeg ? "-" : "") + reverseStr(n)
}
function biToDecimal(i) {
	var t = new BigInt;
	t.digits[0] = 10;
	for (var r = biDivideModulo(i, t), e = String(r[1].digits[0]); 1 == biCompare(r[0], bigZero);) r = biDivideModulo(r[0], t), e += String(r[1].digits[0]);
	return (i.isNeg ? "-" : "") + reverseStr(e)
}
function digitToHex(t) {
	var r = 15,
		e = "";
	for (i = 0; i < 4; ++i) e += hexToChar[t & r], t >>>= 4;
	return reverseStr(e)
}
function biToHex(i) {
	for (var t = "", r = (biHighIndex(i), biHighIndex(i)); r > -1; --r) t += digitToHex(i.digits[r]);
	return t
}
function charToHex(i) {
	var t, r = 48,
		e = r + 9,
		n = 97,
		g = n + 25,
		s = 65,
		d = 90;
	return t = i >= r && i <= e ? i - r : i >= s && i <= d ? 10 + i - s : i >= n && i <= g ? 10 + i - n : 0
}
function hexToDigit(i) {
	for (var t = 0, r = Math.min(i.length, 4), e = 0; e < r; ++e) t <<= 4, t |= charToHex(i.charCodeAt(e));
	return t
}
function biFromHex(i) {
	for (var t = new BigInt, r = i.length, e = r, n = 0; e > 0; e -= 4, ++n) t.digits[n] = hexToDigit(i.substr(Math.max(e - 4, 0), Math.min(e, 4)));
	return t
}
function biFromString(i, t) {
	var r = "-" == i.charAt(0),
		e = r ? 1 : 0,
		n = new BigInt,
		g = new BigInt;
	g.digits[0] = 1;
	for (var s = i.length - 1; s >= e; s--) {
		var d = i.charCodeAt(s),
			o = charToHex(d),
			a = biMultiplyDigit(g, o);
		n = biAdd(n, a), g = biMultiplyDigit(g, t)
	}
	return n.isNeg = r, n
}
function biToBytes(i) {
	for (var t = "", r = biHighIndex(i); r > -1; --r) t += digitToBytes(i.digits[r]);
	return t
}
function digitToBytes(i) {
	var t = String.fromCharCode(255 & i);
	i >>>= 8;
	var r = String.fromCharCode(255 & i);
	return r + t
}
function biDump(i) {
	return (i.isNeg ? "-" : "") + i.digits.join(" ")
}
function biAdd(i, t) {
	var r;
	if (i.isNeg != t.isNeg) t.isNeg = !t.isNeg, r = biSubtract(i, t), t.isNeg = !t.isNeg;
	else {
		r = new BigInt;
		for (var e, n = 0, g = 0; g < i.digits.length; ++g) e = i.digits[g] + t.digits[g] + n, r.digits[g] = 65535 & e, n = Number(e >= biRadix);
		r.isNeg = i.isNeg
	}
	return r
}
function biSubtract(i, t) {
	var r;
	if (i.isNeg != t.isNeg) t.isNeg = !t.isNeg, r = biAdd(i, t), t.isNeg = !t.isNeg;
	else {
		r = new BigInt;
		var e, n;
		n = 0;
		for (var g = 0; g < i.digits.length; ++g) e = i.digits[g] - t.digits[g] + n, r.digits[g] = 65535 & e, r.digits[g] < 0 && (r.digits[g] += biRadix), n = 0 - Number(e < 0);
		if (n == -1) {
			n = 0;
			for (var g = 0; g < i.digits.length; ++g) e = 0 - r.digits[g] + n, r.digits[g] = 65535 & e, r.digits[g] < 0 && (r.digits[g] += biRadix), n = 0 - Number(e < 0);
			r.isNeg = !i.isNeg
		} else r.isNeg = i.isNeg
	}
	return r
}
function biHighIndex(i) {
	for (var t = i.digits.length - 1; t > 0 && 0 == i.digits[t];)--t;
	return t
}
function biNumBits(i) {
	var t, r = biHighIndex(i),
		e = i.digits[r],
		n = (r + 1) * bitsPerDigit;
	for (t = n; t > n - bitsPerDigit && 0 == (32768 & e); --t) e <<= 1;
	return t
}
function biMultiply(i, t) {
	for (var r, e, n, g = new BigInt, s = biHighIndex(i), d = biHighIndex(t), o = 0; o <= d; ++o) {
		for (r = 0, n = o, j = 0; j <= s; ++j, ++n) e = g.digits[n] + i.digits[j] * t.digits[o] + r, g.digits[n] = e & maxDigitVal, r = e >>> biRadixBits;
		g.digits[o + s + 1] = r
	}
	return g.isNeg = i.isNeg != t.isNeg, g
}
function biMultiplyDigit(i, t) {
	var r, e, n;
	result = new BigInt, r = biHighIndex(i), e = 0;
	for (var g = 0; g <= r; ++g) n = result.digits[g] + i.digits[g] * t + e, result.digits[g] = n & maxDigitVal, e = n >>> biRadixBits;
	return result.digits[1 + r] = e, result
}
function arrayCopy(i, t, r, e, n) {
	for (var g = Math.min(t + n, i.length), s = t, d = e; s < g; ++s, ++d) r[d] = i[s]
}
function biShiftLeft(i, t) {
	var r = Math.floor(t / bitsPerDigit),
		e = new BigInt;
	arrayCopy(i.digits, 0, e.digits, r, e.digits.length - r);
	for (var n = t % bitsPerDigit, g = bitsPerDigit - n, s = e.digits.length - 1, d = s - 1; s > 0; --s, --d) e.digits[s] = e.digits[s] << n & maxDigitVal | (e.digits[d] & highBitMasks[n]) >>> g;
	return e.digits[0] = e.digits[s] << n & maxDigitVal, e.isNeg = i.isNeg, e
}
function biShiftRight(i, t) {
	var r = Math.floor(t / bitsPerDigit),
		e = new BigInt;
	arrayCopy(i.digits, r, e.digits, 0, i.digits.length - r);
	for (var n = t % bitsPerDigit, g = bitsPerDigit - n, s = 0, d = s + 1; s < e.digits.length - 1; ++s, ++d) e.digits[s] = e.digits[s] >>> n | (e.digits[d] & lowBitMasks[n]) << g;
	return e.digits[e.digits.length - 1] >>>= n, e.isNeg = i.isNeg, e
}
function biMultiplyByRadixPower(i, t) {
	var r = new BigInt;
	return arrayCopy(i.digits, 0, r.digits, t, r.digits.length - t), r
}
function biDivideByRadixPower(i, t) {
	var r = new BigInt;
	return arrayCopy(i.digits, t, r.digits, 0, r.digits.length - t), r
}
function biModuloByRadixPower(i, t) {
	var r = new BigInt;
	return arrayCopy(i.digits, 0, r.digits, 0, t), r
}
function biCompare(i, t) {
	if (i.isNeg != t.isNeg) return 1 - 2 * Number(i.isNeg);
	for (var r = i.digits.length - 1; r >= 0; --r) if (i.digits[r] != t.digits[r]) return i.isNeg ? 1 - 2 * Number(i.digits[r] > t.digits[r]) : 1 - 2 * Number(i.digits[r] < t.digits[r]);
	return 0
}
function biDivideModulo(i, t) {
	var r, e, n = biNumBits(i),
		g = biNumBits(t),
		s = t.isNeg;
	if (n < g) return i.isNeg ? (r = biCopy(bigOne), r.isNeg = !t.isNeg, i.isNeg = !1, t.isNeg = !1, e = biSubtract(t, i), i.isNeg = !0, t.isNeg = s) : (r = new BigInt, e = biCopy(i)), new Array(r, e);
	r = new BigInt, e = i;
	for (var d = Math.ceil(g / bitsPerDigit) - 1, o = 0; t.digits[d] < biHalfRadix;) t = biShiftLeft(t, 1), ++o, ++g, d = Math.ceil(g / bitsPerDigit) - 1;
	e = biShiftLeft(e, o), n += o;
	for (var a = Math.ceil(n / bitsPerDigit) - 1, u = biMultiplyByRadixPower(t, a - d); biCompare(e, u) != -1;)++r.digits[a - d], e = biSubtract(e, u);
	for (var b = a; b > d; --b) {
		var l = b >= e.digits.length ? 0 : e.digits[b],
			h = b - 1 >= e.digits.length ? 0 : e.digits[b - 1],
			f = b - 2 >= e.digits.length ? 0 : e.digits[b - 2],
			c = d >= t.digits.length ? 0 : t.digits[d],
			m = d - 1 >= t.digits.length ? 0 : t.digits[d - 1];
		l == c ? r.digits[b - d - 1] = maxDigitVal : r.digits[b - d - 1] = Math.floor((l * biRadix + h) / c);
		for (var x = r.digits[b - d - 1] * (c * biRadix + m), v = l * biRadixSquared + (h * biRadix + f); x > v;)--r.digits[b - d - 1], x = r.digits[b - d - 1] * (c * biRadix | m), v = l * biRadix * biRadix + (h * biRadix + f);
		u = biMultiplyByRadixPower(t, b - d - 1), e = biSubtract(e, biMultiplyDigit(u, r.digits[b - d - 1])), e.isNeg && (e = biAdd(e, u), --r.digits[b - d - 1])
	}
	return e = biShiftRight(e, o), r.isNeg = i.isNeg != s, i.isNeg && (r = s ? biAdd(r, bigOne) : biSubtract(r, bigOne), t = biShiftRight(t, o), e = biSubtract(t, e)), 0 == e.digits[0] && 0 == biHighIndex(e) && (e.isNeg = !1), new Array(r, e)
}
function biDivide(i, t) {
	return biDivideModulo(i, t)[0]
}
function biModulo(i, t) {
	return biDivideModulo(i, t)[1]
}
function biMultiplyMod(i, t, r) {
	return biModulo(biMultiply(i, t), r)
}
function biPow(i, t) {
	for (var r = bigOne, e = i;;) {
		if (0 != (1 & t) && (r = biMultiply(r, e)), t >>= 1, 0 == t) break;
		e = biMultiply(e, e)
	}
	return r
}
function biPowMod(i, t, r) {
	for (var e = bigOne, n = i, g = t;;) {
		if (0 != (1 & g.digits[0]) && (e = biMultiplyMod(e, n, r)), g = biShiftRight(g, 1), 0 == g.digits[0] && 0 == biHighIndex(g)) break;
		n = biMultiplyMod(n, n, r)
	}
	return e
}
function RSAKeyPair(i, t, r, e) {
	this.e = biFromHex(i), this.d = biFromHex(t), this.m = biFromHex(r), "number" != typeof e ? this.chunkSize = 2 * biHighIndex(this.m) : this.chunkSize = e / 8, this.radix = 16, this.barrett = new BarrettMu(this.m)
}
function encryptedString(i, t, r, e) {
	var n, g, s, d, o, a, u, b, l, h, f = new Array,
		c = t.length,
		m = "";
	for (d = "string" == typeof r ? r == RSAAPP.NoPadding ? 1 : r == RSAAPP.PKCS1Padding ? 2 : 0 : 0, o = "string" == typeof e && e == RSAAPP.RawEncoding ? 1 : 0, 1 == d ? c > i.chunkSize && (c = i.chunkSize) : 2 == d && c > i.chunkSize - 11 && (c = i.chunkSize - 11), n = 0, g = 2 == d ? c - 1 : i.chunkSize - 1; n < c;) d ? f[g] = t.charCodeAt(n) : f[n] = t.charCodeAt(n), n++, g--;
	for (1 == d && (n = 0), g = i.chunkSize - c % i.chunkSize; g > 0;) {
		if (2 == d) {
			for (a = Math.floor(256 * Math.random()); !a;) a = Math.floor(256 * Math.random());
			f[n] = a
		} else f[n] = 0;
		n++, g--
	}
	for (2 == d && (f[c] = 0, f[i.chunkSize - 2] = 2, f[i.chunkSize - 1] = 0), u = f.length, n = 0; n < u; n += i.chunkSize) {
		for (b = new BigInt, g = 0, s = n; s < n + i.chunkSize; ++g) b.digits[g] = f[s++], b.digits[g] += f[s++] << 8;
		l = i.barrett.powMod(b, i.e), h = 1 == o ? biToBytes(l) : 16 == i.radix ? biToHex(l) : biToString(l, i.radix), m += h
	}
	return m
}
function decryptedString(i, t) {
	var r, e, n, g, s = t.split(" "),
		d = "";
	for (e = 0; e < s.length; ++e) for (g = 16 == i.radix ? biFromHex(s[e]) : biFromString(s[e], i.radix), r = i.barrett.powMod(g, i.d), n = 0; n <= biHighIndex(r); ++n) d += String.fromCharCode(255 & r.digits[n], r.digits[n] >> 8);
	return 0 == d.charCodeAt(d.length - 1) && (d = d.substring(0, d.length - 1)), d
}
var biRadixBase = 2,
	biRadixBits = 16,
	bitsPerDigit = biRadixBits,
	biRadix = 65536,
	biHalfRadix = biRadix >>> 1,
	biRadixSquared = biRadix * biRadix,
	maxDigitVal = biRadix - 1,
	maxInteger = 9999999999999998,
	maxDigits, ZERO_ARRAY, bigZero, bigOne;
setMaxDigits(20);
var dpl10 = 15,
	lr10 = biFromNumber(1e15),
	hexatrigesimalToChar = new Array("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"),
	hexToChar = new Array("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"),
	highBitMasks = new Array(0, 32768, 49152, 57344, 61440, 63488, 64512, 65024, 65280, 65408, 65472, 65504, 65520, 65528, 65532, 65534, 65535),
	lowBitMasks = new Array(0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535),
	RSAAPP = {};
RSAAPP.NoPadding = "NoPadding", RSAAPP.PKCS1Padding = "PKCS1Padding", RSAAPP.RawEncoding = "RawEncoding", RSAAPP.NumericEncoding = "NumericEncoding", function() {
	function i(i) {
		var t = new Image,
			r = "";
		for (var e in i) r += "&" + e + "=" + encodeURIComponent(i[e]);
		r = "https://wlmonitor.m.jd.com/web_login_report?" + r.substring(1), t.src = r
	}
	function t(i, r) {
		if ("object" == typeof r && null != r) for (var e in r)"object" == typeof r[e] ? (i[e] = r[e].length ? [] : {}, t(i[e], r[e])) : i[e] = r[e]
	}
	function r(i) {
		for (var t = location.search.substring(1), r = t.split("&"), e = {}, n = 0; n < r.length; n++) {
			var g = r[n].split("=");
			e[g[0]] = g[1]
		}
		return e[i] ? e[i] : ""
	}
	function e(i) {
		var t = document.cookie.match(new RegExp("(^| )" + i + "=([^;]*)($|;)"));
		return t ? decodeURIComponent(t[2]) : ""
	}
	var n = function(n) {
			var g = r("appid"),
				s = e("guid"),
				d = e("pin"),
				o = {
					appID: g ? parseInt(g, 10) : 100,
					interfaceID: 0,
					loginName: "",
					uuid: s,
					pin: d,
					guid: s,
					os: "5",
					netType: "",
					appVersion: "1.3.0",
					status: "",
					callTime: 0
				};
			t(o, n), i(o)
		};
	
}

function u(){
     var e = {};var t =\'''' + self.str_rsaString + '''\';setMaxDigits(131);var n = new RSAKeyPair("3", "10001", t, 1024),i = encryptedString(n,\'''' + pwd + '\', RSAAPP.PKCS1Padding, RSAAPP.RawEncoding);return i}'
        ctxt = PyV8.JSContext()
        ctxt.enter()
        a=a.decode('utf8')
        ctxt.eval(a)
        func = ctxt.locals.u

        #需要处理一次window.btoa()的python实现
        a = base64.b64encode(func()) #base 64 函数结果与抓包结果长度不同


        return a

    def get_dat(self, username, pwd):
        md5 = """
        function md5(string){
                        function md5_RotateLeft(lValue, iShiftBits) {
                                return (lValue<<iShiftBits) | (lValue>>>(32-iShiftBits));
                        }
                        function md5_AddUnsigned(lX,lY){
                                var lX4,lY4,lX8,lY8,lResult;
                                lX8 = (lX & 0x80000000);
                                lY8 = (lY & 0x80000000);
                                lX4 = (lX & 0x40000000);
                                lY4 = (lY & 0x40000000);
                                lResult = (lX & 0x3FFFFFFF)+(lY & 0x3FFFFFFF);
                                if (lX4 & lY4) {
                                        return (lResult ^ 0x80000000 ^ lX8 ^ lY8);
                                }
                                if (lX4 | lY4) {
                                        if (lResult & 0x40000000) {
                                                return (lResult ^ 0xC0000000 ^ lX8 ^ lY8);
                                        } else {
                                                return (lResult ^ 0x40000000 ^ lX8 ^ lY8);
                                        }
                                } else {
                                        return (lResult ^ lX8 ^ lY8);
                                }
                        }         
                        function md5_F(x,y,z){
                                return (x & y) | ((~x) & z);
                        }
                        function md5_G(x,y,z){
                                return (x & z) | (y & (~z));
                        }
                        function md5_H(x,y,z){
                                return (x ^ y ^ z);
                        }
                        function md5_I(x,y,z){
                                return (y ^ (x | (~z)));
                        }
                        function md5_FF(a,b,c,d,x,s,ac){
                                a = md5_AddUnsigned(a, md5_AddUnsigned(md5_AddUnsigned(md5_F(b, c, d), x), ac));
                                return md5_AddUnsigned(md5_RotateLeft(a, s), b);
                        }; 
                        function md5_GG(a,b,c,d,x,s,ac){
                                a = md5_AddUnsigned(a, md5_AddUnsigned(md5_AddUnsigned(md5_G(b, c, d), x), ac));
                                return md5_AddUnsigned(md5_RotateLeft(a, s), b);
                        };
                        function md5_HH(a,b,c,d,x,s,ac){
                                a = md5_AddUnsigned(a, md5_AddUnsigned(md5_AddUnsigned(md5_H(b, c, d), x), ac));
                                return md5_AddUnsigned(md5_RotateLeft(a, s), b);
                        }; 
                        function md5_II(a,b,c,d,x,s,ac){
                                a = md5_AddUnsigned(a, md5_AddUnsigned(md5_AddUnsigned(md5_I(b, c, d), x), ac));
                                return md5_AddUnsigned(md5_RotateLeft(a, s), b);
                        };
                        function md5_ConvertToWordArray(string) {
                                var lWordCount;
                                var lMessageLength = string.length;
                                var lNumberOfWords_temp1=lMessageLength + 8;
                                var lNumberOfWords_temp2=(lNumberOfWords_temp1-(lNumberOfWords_temp1 % 64))/64;
                                var lNumberOfWords = (lNumberOfWords_temp2+1)*16;
                                var lWordArray=Array(lNumberOfWords-1);
                                var lBytePosition = 0;
                                var lByteCount = 0;
                                while ( lByteCount < lMessageLength ) {
                                        lWordCount = (lByteCount-(lByteCount % 4))/4;
                                        lBytePosition = (lByteCount % 4)*8;
                                        lWordArray[lWordCount] = (lWordArray[lWordCount] | (string.charCodeAt(lByteCount)<<lBytePosition));
                                        lByteCount++;
                                }
                                lWordCount = (lByteCount-(lByteCount % 4))/4;
                                lBytePosition = (lByteCount % 4)*8;
                                lWordArray[lWordCount] = lWordArray[lWordCount] | (0x80<<lBytePosition);
                                lWordArray[lNumberOfWords-2] = lMessageLength<<3;
                                lWordArray[lNumberOfWords-1] = lMessageLength>>>29;
                                return lWordArray;
                        }; 
                        function md5_WordToHex(lValue){
                                var WordToHexValue="",WordToHexValue_temp="",lByte,lCount;
                                for(lCount = 0;lCount<=3;lCount++){
                                        lByte = (lValue>>>(lCount*8)) & 255;
                                        WordToHexValue_temp = "0" + lByte.toString(16);
                                        WordToHexValue = WordToHexValue + WordToHexValue_temp.substr(WordToHexValue_temp.length-2,2);
                                }
                                return WordToHexValue;
                        };
                        function md5_Utf8Encode(string){
                                string = string.replace(/\\r\\n/g,"\\n");
                                var utftext = ""; 
                                for (var n = 0; n < string.length; n++) {
                                        var c = string.charCodeAt(n); 
                                        if (c < 128) {
                                                utftext += String.fromCharCode(c);
                                        }else if((c > 127) && (c < 2048)) {
                                                utftext += String.fromCharCode((c >> 6) | 192);
                                                utftext += String.fromCharCode((c & 63) | 128);
                                        } else {
                                                utftext += String.fromCharCode((c >> 12) | 224);
                                                utftext += String.fromCharCode(((c >> 6) & 63) | 128);
                                                utftext += String.fromCharCode((c & 63) | 128);
                                        } 
                                } 
                                return utftext;
                        }; 
                        var x=Array();
                        var k,AA,BB,CC,DD,a,b,c,d;
                        var S11=7, S12=12, S13=17, S14=22;
                        var S21=5, S22=9 , S23=14, S24=20;
                        var S31=4, S32=11, S33=16, S34=23;
                        var S41=6, S42=10, S43=15, S44=21;
                        string = md5_Utf8Encode(string);
                        x = md5_ConvertToWordArray(string); 
                        a = 0x67452301; b = 0xEFCDAB89; c = 0x98BADCFE; d = 0x10325476; 
                        for (k=0;k<x.length;k+=16) {
                                AA=a; BB=b; CC=c; DD=d;
                                a=md5_FF(a,b,c,d,x[k+0], S11,0xD76AA478);
                                d=md5_FF(d,a,b,c,x[k+1], S12,0xE8C7B756);
                                c=md5_FF(c,d,a,b,x[k+2], S13,0x242070DB);
                                b=md5_FF(b,c,d,a,x[k+3], S14,0xC1BDCEEE);
                                a=md5_FF(a,b,c,d,x[k+4], S11,0xF57C0FAF);
                                d=md5_FF(d,a,b,c,x[k+5], S12,0x4787C62A);
                                c=md5_FF(c,d,a,b,x[k+6], S13,0xA8304613);
                                b=md5_FF(b,c,d,a,x[k+7], S14,0xFD469501);
                                a=md5_FF(a,b,c,d,x[k+8], S11,0x698098D8);
                                d=md5_FF(d,a,b,c,x[k+9], S12,0x8B44F7AF);
                                c=md5_FF(c,d,a,b,x[k+10],S13,0xFFFF5BB1);
                                b=md5_FF(b,c,d,a,x[k+11],S14,0x895CD7BE);
                                a=md5_FF(a,b,c,d,x[k+12],S11,0x6B901122);
                                d=md5_FF(d,a,b,c,x[k+13],S12,0xFD987193);
                                c=md5_FF(c,d,a,b,x[k+14],S13,0xA679438E);
                                b=md5_FF(b,c,d,a,x[k+15],S14,0x49B40821);
                                a=md5_GG(a,b,c,d,x[k+1], S21,0xF61E2562);
                                d=md5_GG(d,a,b,c,x[k+6], S22,0xC040B340);
                                c=md5_GG(c,d,a,b,x[k+11],S23,0x265E5A51);
                                b=md5_GG(b,c,d,a,x[k+0], S24,0xE9B6C7AA);
                                a=md5_GG(a,b,c,d,x[k+5], S21,0xD62F105D);
                                d=md5_GG(d,a,b,c,x[k+10],S22,0x2441453);
                                c=md5_GG(c,d,a,b,x[k+15],S23,0xD8A1E681);
                                b=md5_GG(b,c,d,a,x[k+4], S24,0xE7D3FBC8);
                                a=md5_GG(a,b,c,d,x[k+9], S21,0x21E1CDE6);
                                d=md5_GG(d,a,b,c,x[k+14],S22,0xC33707D6);
                                c=md5_GG(c,d,a,b,x[k+3], S23,0xF4D50D87);
                                b=md5_GG(b,c,d,a,x[k+8], S24,0x455A14ED);
                                a=md5_GG(a,b,c,d,x[k+13],S21,0xA9E3E905);
                                d=md5_GG(d,a,b,c,x[k+2], S22,0xFCEFA3F8);
                                c=md5_GG(c,d,a,b,x[k+7], S23,0x676F02D9);
                                b=md5_GG(b,c,d,a,x[k+12],S24,0x8D2A4C8A);
                                a=md5_HH(a,b,c,d,x[k+5], S31,0xFFFA3942);
                                d=md5_HH(d,a,b,c,x[k+8], S32,0x8771F681);
                                c=md5_HH(c,d,a,b,x[k+11],S33,0x6D9D6122);
                                b=md5_HH(b,c,d,a,x[k+14],S34,0xFDE5380C);
                                a=md5_HH(a,b,c,d,x[k+1], S31,0xA4BEEA44);
                                d=md5_HH(d,a,b,c,x[k+4], S32,0x4BDECFA9);
                                c=md5_HH(c,d,a,b,x[k+7], S33,0xF6BB4B60);
                                b=md5_HH(b,c,d,a,x[k+10],S34,0xBEBFBC70);
                                a=md5_HH(a,b,c,d,x[k+13],S31,0x289B7EC6);
                                d=md5_HH(d,a,b,c,x[k+0], S32,0xEAA127FA);
                                c=md5_HH(c,d,a,b,x[k+3], S33,0xD4EF3085);
                                b=md5_HH(b,c,d,a,x[k+6], S34,0x4881D05);
                                a=md5_HH(a,b,c,d,x[k+9], S31,0xD9D4D039);
                                d=md5_HH(d,a,b,c,x[k+12],S32,0xE6DB99E5);
                                c=md5_HH(c,d,a,b,x[k+15],S33,0x1FA27CF8);
                                b=md5_HH(b,c,d,a,x[k+2], S34,0xC4AC5665);
                                a=md5_II(a,b,c,d,x[k+0], S41,0xF4292244);
                                d=md5_II(d,a,b,c,x[k+7], S42,0x432AFF97);
                                c=md5_II(c,d,a,b,x[k+14],S43,0xAB9423A7);
                                b=md5_II(b,c,d,a,x[k+5], S44,0xFC93A039);
                                a=md5_II(a,b,c,d,x[k+12],S41,0x655B59C3);
                                d=md5_II(d,a,b,c,x[k+3], S42,0x8F0CCC92);
                                c=md5_II(c,d,a,b,x[k+10],S43,0xFFEFF47D);
                                b=md5_II(b,c,d,a,x[k+1], S44,0x85845DD1);
                                a=md5_II(a,b,c,d,x[k+8], S41,0x6FA87E4F);
                                d=md5_II(d,a,b,c,x[k+15],S42,0xFE2CE6E0);
                                c=md5_II(c,d,a,b,x[k+6], S43,0xA3014314);
                                b=md5_II(b,c,d,a,x[k+13],S44,0x4E0811A1);
                                a=md5_II(a,b,c,d,x[k+4], S41,0xF7537E82);
                                d=md5_II(d,a,b,c,x[k+11],S42,0xBD3AF235);
                                c=md5_II(c,d,a,b,x[k+2], S43,0x2AD7D2BB);
                                b=md5_II(b,c,d,a,x[k+9], S44,0xEB86D391);
                                a=md5_AddUnsigned(a,AA);
                                b=md5_AddUnsigned(b,BB);
                                c=md5_AddUnsigned(c,CC);
                                d=md5_AddUnsigned(d,DD);
                        }
                return (md5_WordToHex(a)+md5_WordToHex(b)+md5_WordToHex(c)+md5_WordToHex(d)).toLowerCase();
        }
        function getDat(username,pwd)
        """
        ctxt = PyV8.JSContext()
        ctxt.enter()
        random = re.findall('function getDat\(username,pwd\)(.*?)  ', self.html, re.S)[0]
        ctxt.eval(md5 + random)
        func = ctxt.locals.getDat
        return func(username, pwd)


t = mjdLogin('#', '#')

