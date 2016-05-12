/* start module: primer */
$pyjs['loaded_modules']['primer'] = function (__mod_name__) {
	if($pyjs['loaded_modules']['primer']['__was_initialized__']) return $pyjs['loaded_modules']['primer'];
	var $m = $pyjs['loaded_modules']['primer'];
	$m['__repr__'] = function() { return '<module: primer>'; };
	$m['__was_initialized__'] = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'primer';
	$m['__name__'] = __mod_name__;


	$m['pyjd'] = $p['___import___']('pyjd', null);
	$m['RootPanel'] = $p['___import___']('pyjamas.ui.RootPanel.RootPanel', null, null, false);
	$m['Label'] = $p['___import___']('pyjamas.ui.Label.Label', null, null, false);
	$m['Button'] = $p['___import___']('pyjamas.ui.Button.Button', null, null, false);
	$m['TextBox'] = $p['___import___']('pyjamas.ui.TextBox.TextBox', null, null, false);
	$m['HTTPRequest'] = $p['___import___']('pyjamas.HTTPRequest.HTTPRequest', null, null, false);
	$m['loads'] = $p['___import___']('pyjamas.JSONService.loads', null, null, false);
	$m['pygwt'] = $p['___import___']('pygwt', null);
	$m['cont'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition['__module__'] = 'primer';
		$method = $pyjs__bind_method2('onCompletion', function(text) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				text = arguments[1];
			}
			var data;
			data = $m['loads'](text);
			if ($p['bool'](data['has_key']('title'))) {
				$m['movieLabel']['setText'](data['__getitem__']('title'));
			}
			else {
				$m['movieLabel']['setText']('Error: Movie ID not found.');
			}
			return null;
		}
	, 1, [null,null,['self'],['text']]);
		$cls_definition['onCompletion'] = $method;
		$method = $pyjs__bind_method2('onError', function(text, code) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				text = arguments[1];
				code = arguments[2];
			}
			var data;
			data = $m['loads'](text);
			$m['movieLabel']['setText']('Error: HTTP Get Request');
			return null;
		}
	, 1, [null,null,['self'],['text'],['code']]);
		$cls_definition['onError'] = $method;
		var $bases = new Array(pyjslib['object']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data['__setitem__']($item, $cls_definition[$item]); }
		return $p['_create_class']('cont', $p['tuple']($bases), $data);
	})();
	$m['buttonHandler'] = function(self) {
		var mId,$add2,$add1,$pyjs_try_err,x;
		mId = $m['userText']['getText']();
		try {
			x = $p['float_int'](mId);
			$m['HTTPRequest']()['asyncGet']($p['__op_add']($add1='http://student00.cse.nd.edu:40001/movies/',$add2=$p['str'](mId)), $m['cont'](self));
		} catch($pyjs_try_err) {
			var $pyjs_try_err_name = (typeof $pyjs_try_err['__name__'] == 'undefined' ? $pyjs_try_err['name'] : $pyjs_try_err['__name__'] );
			$pyjs['__last_exception__'] = {'error': $pyjs_try_err, 'module': $m};
			if (true) {
				$m['movieLabel']['setText']('Error: Enter an integer for the movie ID.');
			}
		}
		return null;
	};
	$m['buttonHandler']['__name__'] = 'buttonHandler';

	$m['buttonHandler']['__bind_type__'] = 0;
	$m['buttonHandler']['__args__'] = [null,null,['self']];
	if ($p['bool']($p['op_eq']((typeof __name__ == "undefined"?$m['__name__']:__name__), '__main__'))) {
		$m['pyjd']['setup']('public/primer.html');
		$m['instLabel'] = $pyjs_kwargs_call(null, $m['Label'], null, null, [{'StyleName':'teststyle'}, 'Enter movie ID:']);
		$m['userText'] = $pyjs_kwargs_call(null, $m['TextBox'], null, null, [{'StyleName':'teststyle'}, '']);
		$m['clickButton'] = $m['Button']('Click Here', $m['buttonHandler']);
		$m['movieLabel'] = $m['Label']();
		$m['RootPanel']()['add']($m['instLabel']);
		$m['RootPanel']()['add']($m['userText']);
		$m['RootPanel']()['add']($m['clickButton']);
		$m['RootPanel']()['add']($m['movieLabel']);
		$m['pyjd']['run']();
	}
	return this;
}; /* end primer */


/* end module: primer */


/*
PYJS_DEPS: ['pyjd', 'pyjamas.ui.RootPanel.RootPanel', 'pyjamas', 'pyjamas.ui', 'pyjamas.ui.RootPanel', 'pyjamas.ui.Label.Label', 'pyjamas.ui.Label', 'pyjamas.ui.Button.Button', 'pyjamas.ui.Button', 'pyjamas.ui.TextBox.TextBox', 'pyjamas.ui.TextBox', 'pyjamas.HTTPRequest.HTTPRequest', 'pyjamas.HTTPRequest', 'pyjamas.JSONService.loads', 'pyjamas.JSONService', 'pygwt']
*/
