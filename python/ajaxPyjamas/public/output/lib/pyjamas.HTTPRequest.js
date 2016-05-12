/* start module: pyjamas.HTTPRequest */
$pyjs['loaded_modules']['pyjamas.HTTPRequest'] = function (__mod_name__) {
	if($pyjs['loaded_modules']['pyjamas.HTTPRequest']['__was_initialized__']) return $pyjs['loaded_modules']['pyjamas.HTTPRequest'];
	if(typeof $pyjs['loaded_modules']['pyjamas'] == 'undefined' || !$pyjs['loaded_modules']['pyjamas']['__was_initialized__']) $p['___import___']('pyjamas', null);
	var $m = $pyjs['loaded_modules']['pyjamas.HTTPRequest'];
	$m['__repr__'] = function() { return '<module: pyjamas.HTTPRequest>'; };
	$m['__was_initialized__'] = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'pyjamas.HTTPRequest';
	$m['__name__'] = __mod_name__;
	$pyjs['loaded_modules']['pyjamas']['HTTPRequest'] = $pyjs['loaded_modules']['pyjamas.HTTPRequest'];


	$m['pyjd'] = $p['___import___']('pyjd', 'pyjamas');
	$m['pygwt'] = $p['___import___']('pygwt', 'pyjamas');
	if ($p['bool']($p['getattr']($m['pyjd'], 'is_desktop'))) {
	}
	$m['sys'] = $p['___import___']('sys', 'pyjamas');
	$m['handlers'] = $p['dict']([]);
	$m['XULrunnerHackCallback'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition['__module__'] = 'pyjamas.HTTPRequest';
		$method = $pyjs__bind_method2('__init__', function(htr, mode, user, pwd, url, postData, handler, return_xml, content_type, headers) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				htr = arguments[1];
				mode = arguments[2];
				user = arguments[3];
				pwd = arguments[4];
				url = arguments[5];
				postData = arguments[6];
				handler = arguments[7];
				return_xml = arguments[8];
				content_type = arguments[9];
				headers = arguments[10];
			}
			if (typeof postData == 'undefined') postData=arguments['callee']['__args__'][8][1];
			if (typeof handler == 'undefined') handler=arguments['callee']['__args__'][9][1];
			if (typeof return_xml == 'undefined') return_xml=arguments['callee']['__args__'][10][1];
			if (typeof content_type == 'undefined') content_type=arguments['callee']['__args__'][11][1];
			if (typeof headers == 'undefined') headers=arguments['callee']['__args__'][12][1];

 			return null;
		}
	, 1, [null,null,['self'],['htr'],['mode'],['user'],['pwd'],['url'],['postData', null],['handler', null],['return_xml', false],['content_type', null],['headers', null]]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('callback', function() {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			return self['htr']['asyncImpl']($p['getattr'](self, 'mode'), $p['getattr'](self, 'user'), $p['getattr'](self, 'pwd'), $p['getattr'](self, 'url'), $p['getattr'](self, 'postData'), $p['getattr'](self, 'handler'), $p['getattr'](self, 'return_xml'), $p['getattr'](self, 'content_type'), $p['getattr'](self, 'headers'));
		}
	, 1, [null,null,['self']]);
		$cls_definition['callback'] = $method;
		var $bases = new Array($p['object']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data['__setitem__']($item, $cls_definition[$item]); }
		return $p['_create_class']('XULrunnerHackCallback', $p['tuple']($bases), $data);
	})();
	$m['HTTPRequest'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition['__module__'] = 'pyjamas.HTTPRequest';
		$method = $pyjs__bind_method2('asyncGet', function(url, handler, returnxml, content_type, headers, user, pwd) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				url = arguments[1];
				handler = arguments[2];
				returnxml = arguments[3];
				content_type = arguments[4];
				headers = arguments[5];
				user = arguments[6];
				pwd = arguments[7];
			}
			if (typeof returnxml == 'undefined') returnxml=arguments['callee']['__args__'][5][1];
			if (typeof content_type == 'undefined') content_type=arguments['callee']['__args__'][6][1];
			if (typeof headers == 'undefined') headers=arguments['callee']['__args__'][7][1];
			if (typeof user == 'undefined') user=arguments['callee']['__args__'][8][1];
			if (typeof pwd == 'undefined') pwd=arguments['callee']['__args__'][9][1];
			var postData;
			postData = null;
			if ($p['bool'](!$p['bool']($p['hasattr'](handler, 'onCompletion')))) {
				throw ($p['RuntimeError']('Invalid call to asyncGet: handler is not a valid request handler'));
			}
			return self['asyncImpl']('GET', user, pwd, url, postData, handler, returnxml, content_type, headers);
		}
	, 1, [null,null,['self'],['url'],['handler'],['returnxml', false],['content_type', null],['headers', null],['user', null],['pwd', null]]);
		$cls_definition['asyncGet'] = $method;
		$method = $pyjs__bind_method2('asyncPost', function(url, postData, handler, returnxml, content_type, headers, user, pwd) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				url = arguments[1];
				postData = arguments[2];
				handler = arguments[3];
				returnxml = arguments[4];
				content_type = arguments[5];
				headers = arguments[6];
				user = arguments[7];
				pwd = arguments[8];
			}
			if (typeof returnxml == 'undefined') returnxml=arguments['callee']['__args__'][6][1];
			if (typeof content_type == 'undefined') content_type=arguments['callee']['__args__'][7][1];
			if (typeof headers == 'undefined') headers=arguments['callee']['__args__'][8][1];
			if (typeof user == 'undefined') user=arguments['callee']['__args__'][9][1];
			if (typeof pwd == 'undefined') pwd=arguments['callee']['__args__'][10][1];

			if ($p['bool'](!$p['bool']($p['hasattr'](handler, 'onCompletion')))) {
				throw ($p['RuntimeError']('Invalid call to asyncPost: handler is not a valid request handler'));
			}
			return self['asyncImpl']('POST', user, pwd, url, postData, handler, returnxml, content_type, headers);
		}
	, 1, [null,null,['self'],['url'],['postData'],['handler'],['returnxml', false],['content_type', null],['headers', null],['user', null],['pwd', null]]);
		$cls_definition['asyncPost'] = $method;
		$method = $pyjs__bind_method2('asyncDelete', function(url, handler, returnxml, content_type, headers, user, pwd) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				url = arguments[1];
				handler = arguments[2];
				returnxml = arguments[3];
				content_type = arguments[4];
				headers = arguments[5];
				user = arguments[6];
				pwd = arguments[7];
			}
			if (typeof returnxml == 'undefined') returnxml=arguments['callee']['__args__'][5][1];
			if (typeof content_type == 'undefined') content_type=arguments['callee']['__args__'][6][1];
			if (typeof headers == 'undefined') headers=arguments['callee']['__args__'][7][1];
			if (typeof user == 'undefined') user=arguments['callee']['__args__'][8][1];
			if (typeof pwd == 'undefined') pwd=arguments['callee']['__args__'][9][1];
			var postData;
			postData = null;
			if ($p['bool'](!$p['bool']($p['hasattr'](handler, 'onCompletion')))) {
				throw ($p['RuntimeError']('Invalid call to asyncDelete: handler is not a valid request handler'));
			}
			return self['asyncImpl']('DELETE', user, pwd, url, postData, handler, returnxml, content_type, headers);
		}
	, 1, [null,null,['self'],['url'],['handler'],['returnxml', false],['content_type', null],['headers', null],['user', null],['pwd', null]]);
		$cls_definition['asyncDelete'] = $method;
		$method = $pyjs__bind_method2('asyncPut', function(url, postData, handler, returnxml, content_type, headers, user, pwd) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				url = arguments[1];
				postData = arguments[2];
				handler = arguments[3];
				returnxml = arguments[4];
				content_type = arguments[5];
				headers = arguments[6];
				user = arguments[7];
				pwd = arguments[8];
			}
			if (typeof returnxml == 'undefined') returnxml=arguments['callee']['__args__'][6][1];
			if (typeof content_type == 'undefined') content_type=arguments['callee']['__args__'][7][1];
			if (typeof headers == 'undefined') headers=arguments['callee']['__args__'][8][1];
			if (typeof user == 'undefined') user=arguments['callee']['__args__'][9][1];
			if (typeof pwd == 'undefined') pwd=arguments['callee']['__args__'][10][1];

			if ($p['bool'](!$p['bool']($p['hasattr'](handler, 'onCompletion')))) {
				throw ($p['RuntimeError']('Invalid call to asyncPut: handler is not a valid request handler'));
			}
			return self['asyncImpl']('PUT', user, pwd, url, postData, handler, returnxml, content_type, headers);
		}
	, 1, [null,null,['self'],['url'],['postData'],['handler'],['returnxml', false],['content_type', null],['headers', null],['user', null],['pwd', null]]);
		$cls_definition['asyncPut'] = $method;
		$method = $pyjs__bind_method2('createXmlHTTPRequest', function() {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			return self['doCreateXmlHTTPRequest']();
		}
	, 1, [null,null,['self']]);
		$cls_definition['createXmlHTTPRequest'] = $method;
		$method = $pyjs__bind_method2('doCreateXmlHTTPRequest', function() {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			return $m['get_main_frame']()['getXmlHttpRequest']();
		}
	, 1, [null,null,['self']]);
		$cls_definition['doCreateXmlHTTPRequest'] = $method;
		$method = $pyjs__bind_method2('onProgress', function(sender, event, ignorearg) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				sender = arguments[1];
				event = arguments[2];
				ignorearg = arguments[3];
			}
			var localHandler,xmlHttp;
			xmlHttp = $p['getattr'](event, 'target');
			localHandler = $m['handlers']['get'](xmlHttp);
			if ($p['bool']($p['hasattr'](localHandler, 'onProgress'))) {
				localHandler['onProgress'](event);
			}
			return null;
		}
	, 1, [null,null,['self'],['sender'],['event'],['ignorearg']]);
		$cls_definition['onProgress'] = $method;
		$method = $pyjs__bind_method2('onLoad', function(sender, event, ignorearg) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				sender = arguments[1];
				event = arguments[2];
				ignorearg = arguments[3];
			}
			var status,localHandler,xmlHttp,$or2,handler,responseText,$or1;
			xmlHttp = $p['getattr'](event, 'target');
			localHandler = $m['handlers']['get'](xmlHttp);
			$m['handlers']['__delitem__'](xmlHttp);
			responseText = $p['getattr'](xmlHttp, 'responseText');
			status = $p['getattr'](xmlHttp, 'status');
			handler = null;
			xmlHttp = null;
			if ($p['bool']($p['op_eq'](status, 0))) {
				$p['printFunc'](['HACK ALERT! webkit wrapper returns 0 not 200!'], 1);
			}
			if ($p['bool'](($p['bool']($or1=$p['op_eq'](status, 200))?$or1:$p['op_eq'](status, 0)))) {
				localHandler['onCompletion'](responseText);
			}
			else {
				localHandler['onError'](responseText, status);
			}
			return null;
		}
	, 1, [null,null,['self'],['sender'],['event'],['ignorearg']]);
		$cls_definition['onLoad'] = $method;
		$method = $pyjs__bind_method2('onReadyStateChange', function(xmlHttp, event, ignorearg) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				xmlHttp = arguments[1];
				event = arguments[2];
				ignorearg = arguments[3];
			}
			var status,$or4,localHandler,$or3,handler,$pyjs_try_err,responseText;
			try {
				xmlHttp = $m['get_main_frame']()['gobject_wrap'](xmlHttp);
			} catch($pyjs_try_err) {
				var $pyjs_try_err_name = (typeof $pyjs_try_err['__name__'] == 'undefined' ? $pyjs_try_err['name'] : $pyjs_try_err['__name__'] );
				$pyjs['__last_exception__'] = {'error': $pyjs_try_err, 'module': $m};
				if (true) {
				}
			}
			if ($p['bool'](!$p['op_eq']($p['getattr'](xmlHttp, 'readyState'), 4))) {
				return null;
			}
			localHandler = $m['handlers']['get'](xmlHttp);
			$m['handlers']['__delitem__'](xmlHttp);
			responseText = $p['getattr'](xmlHttp, 'responseText');
			status = $p['getattr'](xmlHttp, 'status');
			handler = null;
			xmlHttp = null;
			if ($p['bool'](($p['bool']($or3=$p['op_eq'](status, 200))?$or3:$p['op_eq'](status, 0)))) {
				localHandler['onCompletion'](responseText);
			}
			else {
				localHandler['onError'](responseText, status);
			}
			return null;
		}
	, 1, [null,null,['self'],['xmlHttp'],['event'],['ignorearg']]);
		$cls_definition['onReadyStateChange'] = $method;
		$method = $pyjs__bind_method2('_convertUrlToAbsolute', function(url) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				url = arguments[1];
			}
			var $add4,sep,$and1,$and3,uri,$add2,$add3,$add1,$add6,slash,$add5,$and2;
			uri = $m['pygwt']['getModuleBaseURL']();
			if ($p['bool']($p['op_eq'](url['__getitem__'](0), '/'))) {
				sep = uri['find']('://');
				if ($p['bool'](!$p['bool'](uri['startswith']('file://')))) {
					slash = uri['find']('/', $p['__op_add']($add1=sep,$add2=3));
					if ($p['bool'](($p['cmp'](slash, 0) == 1))) {
						uri = $p['__getslice'](uri, 0, slash);
					}
				}
				return $p['sprintf']('%s%s', $p['tuple']([uri, url]));
			}
			else {
				if ($p['bool'](($p['bool']($and1=!$p['op_eq']($p['__getslice'](url, 0, 7), 'file://'))?($p['bool']($and2=!$p['op_eq']($p['__getslice'](url, 0, 7), 'http://'))?!$p['op_eq']($p['__getslice'](url, 0, 8), 'https://'):$and2):$and1))) {
					slash = uri['rfind']('/');
					return $p['__op_add']($add5=$p['__getslice'](uri, 0, $p['__op_add']($add3=slash,$add4=1)),$add6=url);
				}
			}
			return url;
		}
	, 1, [null,null,['self'],['url']]);
		$cls_definition['_convertUrlToAbsolute'] = $method;
		$method = $pyjs__bind_method2('asyncImpl', function(method, user, pwd, url, postData, handler, returnxml, content_type, headers) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				method = arguments[1];
				user = arguments[2];
				pwd = arguments[3];
				url = arguments[4];
				postData = arguments[5];
				handler = arguments[6];
				returnxml = arguments[7];
				content_type = arguments[8];
				headers = arguments[9];
			}
			if (typeof returnxml == 'undefined') returnxml=arguments['callee']['__args__'][9][1];
			if (typeof content_type == 'undefined') content_type=arguments['callee']['__args__'][10][1];
			if (typeof headers == 'undefined') headers=arguments['callee']['__args__'][11][1];
			var $or5,hval,$iter1_iter,$or8,res,base64,$pyjs_try_err,$iter1_array,$and8,$or7,$or6,$iter1_nextval,$and4,$and5,$and6,$and7,mf,xmlHttp,$iter1_type,h,$iter1_idx;
			if ($p['bool']((headers === null))) {
				headers = $p['dict']([]);
			}
			if ($p['bool'](($p['bool']($and4=user)?($p['bool']($and5=pwd)?!$p['bool'](headers['__contains__']('Authorization')):$and5):$and4))) {
				base64 = $p['___import___']('base64', 'pyjamas');
				headers['__setitem__']('Authorization', $p['sprintf']('Basic %s', base64['b64encode']($p['sprintf']('%s:%s', $p['tuple']([user, pwd])))));
			}
			mf = (typeof get_main_frame == "undefined"?$m['get_main_frame']:get_main_frame)();
			if ($p['bool']((content_type !== null))) {
				headers['__setitem__']('Content-Type', content_type);
			}
			if ($p['bool'](!$p['bool'](headers['__contains__']('Content-Type')))) {
				if ($p['bool'](returnxml)) {
					headers['__setitem__']('Content-Type', 'application/xml; charset=utf-8');
				}
				else {
					headers['__setitem__']('Content-Type', 'text/plain; charset=utf-8');
				}
			}
			xmlHttp = self['doCreateXmlHTTPRequest']();
			url = self['_convertUrlToAbsolute'](url);
			if ($p['bool']($p['op_eq']($p['getattr'](mf, 'platform'), 'webkit'))) {
				mf['_addXMLHttpRequestEventListener'](xmlHttp, 'readystatechange', $p['getattr'](self, 'onReadyStateChange'));
			}
			else if ($p['bool']($p['op_eq']($p['getattr'](mf, 'platform'), 'mshtml'))) {
				mf['_addXMLHttpRequestEventListener'](xmlHttp, 'onreadystatechange', $p['getattr'](self, 'onReadyStateChange'));
			}
			else {
				mf['_addXMLHttpRequestEventListener'](xmlHttp, 'load', $p['getattr'](self, 'onLoad'));
			}
			if ($p['bool'](($p['bool']($and7=!$p['op_eq']($p['getattr'](mf, 'platform'), 'mshtml'))?!$p['op_eq']($p['getattr'](mf, 'platform'), 'ie6'):$and7))) {
				mf['_addXMLHttpRequestEventListener'](xmlHttp, 'progress', $p['getattr'](self, 'onProgress'));
			}
			if ($p['bool'](($p['bool']($or5=$p['op_eq']($p['getattr'](mf, 'platform'), 'webkit'))?$or5:$p['op_eq']($p['getattr'](mf, 'platform'), 'mshtml')))) {
				xmlHttp['open'](method, url, true, '', '');
			}
			else {
				try {
					res = xmlHttp['open'](method, url, true, '', '');
				} catch($pyjs_try_err) {
					var $pyjs_try_err_name = (typeof $pyjs_try_err['__name__'] == 'undefined' ? $pyjs_try_err['name'] : $pyjs_try_err['__name__'] );
					$pyjs['__last_exception__'] = {'error': $pyjs_try_err, 'module': $m};
					if (true) {
						res = xmlHttp['open'](method, url);
					}
				}
			}
			$iter1_iter = headers;
			$iter1_nextval=$p['__iter_prepare']($iter1_iter,false);
			while (typeof($p['__wrapped_next']($iter1_nextval)['$nextval']) != 'undefined') {
				h = $iter1_nextval['$nextval'];
				if ($p['bool']($p['isinstance'](headers['__getitem__'](h), $p['basestring']))) {
					xmlHttp['setRequestHeader'](h, headers['__getitem__'](h));
				}
				else {
					hval = ';'['join'](function(){
						var $iter2_nextval,$iter2_type,$iter2_iter,i,$collcomp1,$iter2_idx,$iter2_array;
	$collcomp1 = $p['list']();
					$iter2_iter = headers['__getitem__'](h);
					$iter2_nextval=$p['__iter_prepare']($iter2_iter,false);
					while (typeof($p['__wrapped_next']($iter2_nextval)['$nextval']) != 'undefined') {
						i = $iter2_nextval['$nextval'];
						$collcomp1['append']($p['str'](i));
					}

	return $collcomp1;}());
					xmlHttp['setRequestHeader'](h, hval);
				}
			}
			$m['handlers']['__setitem__'](xmlHttp, handler);
			try {
				xmlHttp['send'](($p['bool']($or7=postData)?$or7:''));
			} catch($pyjs_try_err) {
				var $pyjs_try_err_name = (typeof $pyjs_try_err['__name__'] == 'undefined' ? $pyjs_try_err['name'] : $pyjs_try_err['__name__'] );
				$pyjs['__last_exception__'] = {'error': $pyjs_try_err, 'module': $m};
				if (true) {
					handler['onError']('xmlHttp.send error', (typeof ($usub1=1)=='number'?
						-$usub1:
						$p['op_usub']($usub1)));
				}
			}
			return xmlHttp;
			handler = null;
			xmlHttp = null;
			$m['localHandler']['onError']($p['str']((typeof e == "undefined"?$m['e']:e)));
			return null;
		}
	, 1, [null,null,['self'],['method'],['user'],['pwd'],['url'],['postData'],['handler'],['returnxml', false],['content_type', null],['headers', null]]);
		$cls_definition['asyncImpl'] = $method;
		var $bases = new Array($p['object']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data['__setitem__']($item, $cls_definition[$item]); }
		return $p['_create_class']('HTTPRequest', $p['tuple']($bases), $data);
	})();
	return this;
}; /* end pyjamas.HTTPRequest */


/* end module: pyjamas.HTTPRequest */


/*
PYJS_DEPS: ['pyjd', 'pygwt', 'sys', 'base64']
*/
