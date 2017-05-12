# coding=utf-8
from .rk import *
from .datacontrol import *
import PyV8
import requests
import re
import random

'''

JD MLogin Module'
Cracked:HiddenStrawberry'

bug:
- USER_FLAG_CHECK and sid was non-existent in cookies(Unable to get coupon)
solution:
- Phantomjs to get and load into cookies

'''

def login(username, pwd, rk_um, rk_pwd):
    url = 'https://passport.m.jd.com/user/login.action?returnurl=https://m.jd.com?indexloc=1'
    cookiestr = ''
    session = requests.session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/54.0.2840.59 Safari/537.36 115Browser/8.0.0',
        'Accept': 'application / json',
    }
    rdname = str(random.randint(1000000, 10000000))
    html = session.get(url, headers=headers, verify=False).text
    str_rsaString = re.findall('str_rsaString = \'(.*?)\'', html, re.S)[0]
    str_kenString = re.findall('str_kenString = \'(.*?)\'', html, re.S)[0]
    authimgurl = 'http://plogin.m.jd.com' + re.findall('<img id="imgCode" src="(.*?)"', html, re.S)[0]
    ir = session.get(authimgurl, headers=headers, verify=False)
    save_img('C:\\temp\\' + rdname + '.png', ir)
    authcode = fuck_code_rk(rk_um, rk_pwd, 'C:\\temp\\' + rdname + '.png')

    datax = {'username': username,
                  'pwd': get_pwd(pwd,str_rsaString),
                  'remember': 'true',
                  's_token': str_kenString,
                  'dat': get_dat(username, pwd,html),
                  'wlfstk_datk': get_dat(username, pwd,html),
                  'authcode': authcode
                  }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/54.0.2840.59 Safari/537.36 115Browser/8.0.0',
        'Referer': url}

    result = session.post('http://plogin.m.jd.com/cgi-bin/m/domlogin', data=datax,
                               headers=headers).text
    errcode = re.findall('"errcode" : (.*?),', result, re.S)[0]
    if errcode == '0':
        print decoder('京东M端登陆成功！')
    else:
        Ex = re.findall('"message" : (.*?),', result, re.S)[0]
        print Ex
        raise Exception('Error!')
    for k, value in session.cookies.items():
        cookiestr = cookiestr + k + '=' + value + ';'
    return cookiestr[:-1]

def get_dat(username, pwd,html):
    md5 = """
    function md5(string){function md5_RotateLeft(lValue,iShiftBits){return(lValue<<iShiftBits)|(lValue>>>(32-iShiftBits))}function md5_AddUnsigned(lX,lY){var lX4,lY4,lX8,lY8,lResult;lX8=(lX&0x80000000);lY8=(lY&0x80000000);lX4=(lX&0x40000000);lY4=(lY&0x40000000);lResult=(lX&0x3FFFFFFF)+(lY&0x3FFFFFFF);if(lX4&lY4){return(lResult^0x80000000^lX8^lY8)}if(lX4|lY4){if(lResult&0x40000000){return(lResult^0xC0000000^lX8^lY8)}else{return(lResult^0x40000000^lX8^lY8)}}else{return(lResult^lX8^lY8)}}function md5_F(x,y,z){return(x&y)|((~x)&z)}function md5_G(x,y,z){return(x&z)|(y&(~z))}function md5_H(x,y,z){return(x^y^z)}function md5_I(x,y,z){return(y^(x|(~z)))}function md5_FF(a,b,c,d,x,s,ac){a=md5_AddUnsigned(a,md5_AddUnsigned(md5_AddUnsigned(md5_F(b,c,d),x),ac));return md5_AddUnsigned(md5_RotateLeft(a,s),b)};function md5_GG(a,b,c,d,x,s,ac){a=md5_AddUnsigned(a,md5_AddUnsigned(md5_AddUnsigned(md5_G(b,c,d),x),ac));return md5_AddUnsigned(md5_RotateLeft(a,s),b)};function md5_HH(a,b,c,d,x,s,ac){a=md5_AddUnsigned(a,md5_AddUnsigned(md5_AddUnsigned(md5_H(b,c,d),x),ac));return md5_AddUnsigned(md5_RotateLeft(a,s),b)};function md5_II(a,b,c,d,x,s,ac){a=md5_AddUnsigned(a,md5_AddUnsigned(md5_AddUnsigned(md5_I(b,c,d),x),ac));return md5_AddUnsigned(md5_RotateLeft(a,s),b)};function md5_ConvertToWordArray(string){var lWordCount;var lMessageLength=string.length;var lNumberOfWords_temp1=lMessageLength+8;var lNumberOfWords_temp2=(lNumberOfWords_temp1-(lNumberOfWords_temp1%64))/64;var lNumberOfWords=(lNumberOfWords_temp2+1)*16;var lWordArray=Array(lNumberOfWords-1);var lBytePosition=0;var lByteCount=0;while(lByteCount<lMessageLength){lWordCount=(lByteCount-(lByteCount%4))/4;lBytePosition=(lByteCount%4)*8;lWordArray[lWordCount]=(lWordArray[lWordCount]|(string.charCodeAt(lByteCount)<<lBytePosition));lByteCount++}lWordCount=(lByteCount-(lByteCount%4))/4;lBytePosition=(lByteCount%4)*8;lWordArray[lWordCount]=lWordArray[lWordCount]|(0x80<<lBytePosition);lWordArray[lNumberOfWords-2]=lMessageLength<<3;lWordArray[lNumberOfWords-1]=lMessageLength>>>29;return lWordArray};function md5_WordToHex(lValue){var WordToHexValue="",WordToHexValue_temp="",lByte,lCount;for(lCount=0;lCount<=3;lCount++){lByte=(lValue>>>(lCount*8))&255;WordToHexValue_temp="0"+lByte.toString(16);WordToHexValue=WordToHexValue+WordToHexValue_temp.substr(WordToHexValue_temp.length-2,2)}return WordToHexValue};function md5_Utf8Encode(string){string=string.replace(/\\r\\n/g,"\\n");var utftext="";for(var n=0;n<string.length;n++){var c=string.charCodeAt(n);if(c<128){utftext+=String.fromCharCode(c)}else if((c>127)&&(c<2048)){utftext+=String.fromCharCode((c>>6)|192);utftext+=String.fromCharCode((c&63)|128)}else{utftext+=String.fromCharCode((c>>12)|224);utftext+=String.fromCharCode(((c>>6)&63)|128);utftext+=String.fromCharCode((c&63)|128)}}return utftext};var x=Array();var k,AA,BB,CC,DD,a,b,c,d;var S11=7,S12=12,S13=17,S14=22;var S21=5,S22=9,S23=14,S24=20;var S31=4,S32=11,S33=16,S34=23;var S41=6,S42=10,S43=15,S44=21;string=md5_Utf8Encode(string);x=md5_ConvertToWordArray(string);a=0x67452301;b=0xEFCDAB89;c=0x98BADCFE;d=0x10325476;for(k=0;k<x.length;k+=16){AA=a;BB=b;CC=c;DD=d;a=md5_FF(a,b,c,d,x[k+0],S11,0xD76AA478);d=md5_FF(d,a,b,c,x[k+1],S12,0xE8C7B756);c=md5_FF(c,d,a,b,x[k+2],S13,0x242070DB);b=md5_FF(b,c,d,a,x[k+3],S14,0xC1BDCEEE);a=md5_FF(a,b,c,d,x[k+4],S11,0xF57C0FAF);d=md5_FF(d,a,b,c,x[k+5],S12,0x4787C62A);c=md5_FF(c,d,a,b,x[k+6],S13,0xA8304613);b=md5_FF(b,c,d,a,x[k+7],S14,0xFD469501);a=md5_FF(a,b,c,d,x[k+8],S11,0x698098D8);d=md5_FF(d,a,b,c,x[k+9],S12,0x8B44F7AF);c=md5_FF(c,d,a,b,x[k+10],S13,0xFFFF5BB1);b=md5_FF(b,c,d,a,x[k+11],S14,0x895CD7BE);a=md5_FF(a,b,c,d,x[k+12],S11,0x6B901122);d=md5_FF(d,a,b,c,x[k+13],S12,0xFD987193);c=md5_FF(c,d,a,b,x[k+14],S13,0xA679438E);b=md5_FF(b,c,d,a,x[k+15],S14,0x49B40821);a=md5_GG(a,b,c,d,x[k+1],S21,0xF61E2562);d=md5_GG(d,a,b,c,x[k+6],S22,0xC040B340);c=md5_GG(c,d,a,b,x[k+11],S23,0x265E5A51);b=md5_GG(b,c,d,a,x[k+0],S24,0xE9B6C7AA);a=md5_GG(a,b,c,d,x[k+5],S21,0xD62F105D);d=md5_GG(d,a,b,c,x[k+10],S22,0x2441453);c=md5_GG(c,d,a,b,x[k+15],S23,0xD8A1E681);b=md5_GG(b,c,d,a,x[k+4],S24,0xE7D3FBC8);a=md5_GG(a,b,c,d,x[k+9],S21,0x21E1CDE6);d=md5_GG(d,a,b,c,x[k+14],S22,0xC33707D6);c=md5_GG(c,d,a,b,x[k+3],S23,0xF4D50D87);b=md5_GG(b,c,d,a,x[k+8],S24,0x455A14ED);a=md5_GG(a,b,c,d,x[k+13],S21,0xA9E3E905);d=md5_GG(d,a,b,c,x[k+2],S22,0xFCEFA3F8);c=md5_GG(c,d,a,b,x[k+7],S23,0x676F02D9);b=md5_GG(b,c,d,a,x[k+12],S24,0x8D2A4C8A);a=md5_HH(a,b,c,d,x[k+5],S31,0xFFFA3942);d=md5_HH(d,a,b,c,x[k+8],S32,0x8771F681);c=md5_HH(c,d,a,b,x[k+11],S33,0x6D9D6122);b=md5_HH(b,c,d,a,x[k+14],S34,0xFDE5380C);a=md5_HH(a,b,c,d,x[k+1],S31,0xA4BEEA44);d=md5_HH(d,a,b,c,x[k+4],S32,0x4BDECFA9);c=md5_HH(c,d,a,b,x[k+7],S33,0xF6BB4B60);b=md5_HH(b,c,d,a,x[k+10],S34,0xBEBFBC70);a=md5_HH(a,b,c,d,x[k+13],S31,0x289B7EC6);d=md5_HH(d,a,b,c,x[k+0],S32,0xEAA127FA);c=md5_HH(c,d,a,b,x[k+3],S33,0xD4EF3085);b=md5_HH(b,c,d,a,x[k+6],S34,0x4881D05);a=md5_HH(a,b,c,d,x[k+9],S31,0xD9D4D039);d=md5_HH(d,a,b,c,x[k+12],S32,0xE6DB99E5);c=md5_HH(c,d,a,b,x[k+15],S33,0x1FA27CF8);b=md5_HH(b,c,d,a,x[k+2],S34,0xC4AC5665);a=md5_II(a,b,c,d,x[k+0],S41,0xF4292244);d=md5_II(d,a,b,c,x[k+7],S42,0x432AFF97);c=md5_II(c,d,a,b,x[k+14],S43,0xAB9423A7);b=md5_II(b,c,d,a,x[k+5],S44,0xFC93A039);a=md5_II(a,b,c,d,x[k+12],S41,0x655B59C3);d=md5_II(d,a,b,c,x[k+3],S42,0x8F0CCC92);c=md5_II(c,d,a,b,x[k+10],S43,0xFFEFF47D);b=md5_II(b,c,d,a,x[k+1],S44,0x85845DD1);a=md5_II(a,b,c,d,x[k+8],S41,0x6FA87E4F);d=md5_II(d,a,b,c,x[k+15],S42,0xFE2CE6E0);c=md5_II(c,d,a,b,x[k+6],S43,0xA3014314);b=md5_II(b,c,d,a,x[k+13],S44,0x4E0811A1);a=md5_II(a,b,c,d,x[k+4],S41,0xF7537E82);d=md5_II(d,a,b,c,x[k+11],S42,0xBD3AF235);c=md5_II(c,d,a,b,x[k+2],S43,0x2AD7D2BB);b=md5_II(b,c,d,a,x[k+9],S44,0xEB86D391);a=md5_AddUnsigned(a,AA);b=md5_AddUnsigned(b,BB);c=md5_AddUnsigned(c,CC);d=md5_AddUnsigned(d,DD)}return(md5_WordToHex(a)+md5_WordToHex(b)+md5_WordToHex(c)+md5_WordToHex(d)).toLowerCase()}
    function getDat(username,pwd)
    """
    ctxt = PyV8.JSContext()
    ctxt.enter()
    rand = re.findall('function getDat\(username,pwd\)(.*?)  ', html, re.S)[0]
    ctxt.eval(md5 + rand)
    func = ctxt.locals.getDat
    return func(username, pwd)

def get_pwd(pwd,str_rsaString):
    a = '''
var base64EncodeChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
function base64encode(str) 
{var out, i, len;
var c1, c2, c3;
len = str.length;
i = 0;
out = "";
while(i < len) {
c1 = str.charCodeAt(i++) & 0xff;
if(i == len)
 {
out += base64EncodeChars.charAt(c1 >> 2);
out += base64EncodeChars.charAt((c1 & 0x3) << 4);
out += "==";
break;
 }
c2 = str.charCodeAt(i++);
if(i == len)
 {
out += base64EncodeChars.charAt(c1 >> 2);
out += base64EncodeChars.charAt(((c1 & 0x3)<< 4) | ((c2 & 0xF0) >> 4));
out += base64EncodeChars.charAt((c2 & 0xF) << 2);
out += "=";
break;
 }
c3 = str.charCodeAt(i++);
out += base64EncodeChars.charAt(c1 >> 2);
out += base64EncodeChars.charAt(((c1 & 0x3)<< 4) | ((c2 & 0xF0) >> 4));
out += base64EncodeChars.charAt(((c2 & 0xF) << 2) | ((c3 & 0xC0) >>6));
out += base64EncodeChars.charAt(c3 & 0x3F);
}
return out;
}

function utf16to8(str) {
var out, i, len, c;
out = "";
len = str.length;
for(i = 0; i < len; i++) {
 c = str.charCodeAt(i);
 if ((c >= 0x0001) && (c <= 0x007F)) {
 out += str.charAt(i);
 } else if (c > 0x07FF) {
 out += String.fromCharCode(0xE0 | ((c >>12) & 0x0F));
 out += String.fromCharCode(0x80 | ((c >>6) & 0x3F));
 out += String.fromCharCode(0x80 | ((c >>0) & 0x3F));
 } else {
 out += String.fromCharCode(0xC0 | ((c >>6) & 0x1F));
 out += String.fromCharCode(0x80 | ((c >>0) & 0x3F));
 }
}
return out;
}
function utf8to16(str) {
var out, i, len, c;
var char2, char3;
out = "";
len = str.length;
i = 0;
while(i < len) {
 c = str.charCodeAt(i++);
 switch(c >> 4)
 {
case 0: case 1: case 2: case 3: case 4: case 5: case 6: case 7:
 // 0xxxxxxx
 out += str.charAt(i-1);
 break;
case 12: case 13:
 // 110x xxxx10xx xxxx
 char2 = str.charCodeAt(i++);
 out += String.fromCharCode(((c & 0x1F) << 6) | (char2 & 0x3F));
 break;
case 14:
 char2 = str.charCodeAt(i++);
 char3 = str.charCodeAt(i++);
 out += String.fromCharCode(((c & 0x0F) << 12) |
((char2 & 0x3F) << 6) |
((char3 & 0x3F) << 0));
 break;
 }
}
return out;
}

function doit() {
var f = document.f
f.output.value = base64encode(utf16to8(f.source.value))
f.decode.value = utf8to16(base64decode(f.output.value))
}        

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
 var e = {};var t ="''' + str_rsaString + '''";setMaxDigits(131);var n = new RSAKeyPair("3", "10001", t, 1024),i = base64encode(encryptedString(n,"''' + pwd + '''", RSAAPP.PKCS1Padding, RSAAPP.RawEncoding));return i}'''



    ctxt = PyV8.JSContext()
    ctxt.enter()
    ctxt.eval(decoder(a))
    func = ctxt.locals.u
    return func()
