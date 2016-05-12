/* start module: movies */
$pyjs['loaded_modules']['movies'] = function (__mod_name__) {
	if($pyjs['loaded_modules']['movies']['__was_initialized__']) return $pyjs['loaded_modules']['movies'];
	var $m = $pyjs['loaded_modules']['movies'];
	$m['__repr__'] = function() { return '<module: movies>'; };
	$m['__was_initialized__'] = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'movies';
	$m['__name__'] = __mod_name__;


	$m['pyjd'] = $p['___import___']('pyjd', null);
	$m['RootPanel'] = $p['___import___']('pyjamas.ui.RootPanel.RootPanel', null, null, false);
	$m['Label'] = $p['___import___']('pyjamas.ui.Label.Label', null, null, false);
	$m['Button'] = $p['___import___']('pyjamas.ui.Button.Button', null, null, false);
	$m['Grid'] = $p['___import___']('pyjamas.ui.Grid.Grid', null, null, false);
	$m['Image'] = $p['___import___']('pyjamas.ui.Image.Image', null, null, false);
	$m['HTTPRequest'] = $p['___import___']('pyjamas.HTTPRequest.HTTPRequest', null, null, false);
	$m['loads'] = $p['___import___']('pyjamas.JSONService.loads', null, null, false);
	$m['dumps'] = $p['___import___']('pyjamas.JSONService.dumps', null, null, false);
	$m['pygwt'] = $p['___import___']('pygwt', null);
	$m['movieInterface'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition['__module__'] = 'movies';
		$method = $pyjs__bind_method2('__init__', function() {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			$pyjs_kwargs_call($p['$$super']($m['movieInterface'], self), '__init__', null, null, [{'rows':4, 'columns':3}]);
			self['uId'] = 3;
			self['mId'] = 1;
			self['API_KEY'] = 'cOBfTz6ZZG';
			self['SERVER_SITE'] = 'http://student00.cse.nd.edu:40001';
			self['mTitle'] = '<title>';
			self['mRating'] = '<rating>';
			self['mPoster'] = '';
			self['eMessage'] = '';
			self['imgIndex'] = 'http://www.cse.nd.edu/~cmc/teaching/cse30332_sp15/images/';
			self['mTitleL'] = $m['Label']();
			self['mRatingL'] = $m['Label']();
			self['upVoteB'] = $m['Button']('UP', $p['getattr'](self, 'upPressed'));
			self['mPosterI'] = $m['Image']();
			self['downVoteB'] = $m['Button']('DOWN', $p['getattr'](self, 'downPressed'));
			self['eMessageL'] = $m['Label']();
			self['setWidget'](0, 1, $p['getattr'](self, 'mTitleL'));
			self['setWidget'](1, 0, $p['getattr'](self, 'upVoteB'));
			self['setWidget'](1, 1, $p['getattr'](self, 'mPosterI'));
			self['setWidget'](1, 2, $p['getattr'](self, 'downVoteB'));
			self['setWidget'](2, 1, $p['getattr'](self, 'mRatingL'));
			self['setWidget'](3, 1, $p['getattr'](self, 'eMessageL'));
			self['getNewMovieRec']();
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('getNewMovieRec', function() {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $add2,$add3,$add1,$add4;
			self['eMessage'] = '';
			$m['HTTPRequest']()['asyncGet']($p['__op_add']($add3=$p['__op_add']($add1=$p['getattr'](self, 'SERVER_SITE'),$add2='/recommendations/'),$add4=$p['str']($p['getattr'](self, 'uId'))), (typeof recControllerGET == "undefined"?$m['recControllerGET']:recControllerGET)(self));
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['getNewMovieRec'] = $method;
		$method = $pyjs__bind_method2('update', function() {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $add6,$add5;
			self['mTitleL']['setText']($p['getattr'](self, 'mTitle'));
			self['mRatingL']['setText']($p['getattr'](self, 'mRating'));
			self['mPosterI']['setUrl']($p['__op_add']($add5=$p['getattr'](self, 'imgIndex'),$add6=$p['getattr'](self, 'mPoster')));
			self['eMessageL']['setText']($p['getattr'](self, 'eMessage'));
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['update'] = $method;
		$method = $pyjs__bind_method2('upPressed', function() {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var text,$add10,$add7,$add8,$add9,data;
			data = $p['dict']([]);
			data['__setitem__']('apikey', $p['getattr'](self, 'API_KEY'));
			data['__setitem__']('movie_id', $p['getattr'](self, 'mId'));
			data['__setitem__']('rating', '5');
			text = $m['dumps'](data);
			$m['HTTPRequest']()['asyncPut']($p['__op_add']($add9=$p['__op_add']($add7=$p['getattr'](self, 'SERVER_SITE'),$add8='/recommendations/'),$add10=$p['str']($p['getattr'](self, 'uId'))), text, (typeof recControllerPUT == "undefined"?$m['recControllerPUT']:recControllerPUT)(self));
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['upPressed'] = $method;
		$method = $pyjs__bind_method2('downPressed', function() {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var text,$add14,$add11,$add12,$add13,data;
			data = $p['dict']([]);
			data['__setitem__']('apikey', $p['getattr'](self, 'API_KEY'));
			data['__setitem__']('movie_id', $p['getattr'](self, 'mId'));
			data['__setitem__']('rating', '5');
			text = $m['dumps'](data);
			$m['HTTPRequest']()['asyncPut']($p['__op_add']($add13=$p['__op_add']($add11=$p['getattr'](self, 'SERVER_SITE'),$add12='/recommendations/'),$add14=$p['str']($p['getattr'](self, 'uId'))), text, (typeof recControllerPUT == "undefined"?$m['recControllerPUT']:recControllerPUT)(self));
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['downPressed'] = $method;
		var $bases = new Array($m['Grid']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data['__setitem__']($item, $cls_definition[$item]); }
		return $p['_create_class']('movieInterface', $p['tuple']($bases), $data);
	})();
	$m['recControllerGET'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition['__module__'] = 'movies';
		$method = $pyjs__bind_method2('__init__', function(interface) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				interface = arguments[1];
			}

			self['main'] = interface;
			return null;
		}
	, 1, [null,null,['self'],['interface']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('onCompletion', function(text) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				text = arguments[1];
			}
			var $add18,$add15,$add16,$add17,data;
			data = $m['loads'](text);
			$p['getattr'](self, 'main')['mId'] = $p['float_int'](data['__getitem__']('movie_id'));
			$m['HTTPRequest']()['asyncGet']($p['__op_add']($add17=$p['__op_add']($add15=$p['getattr']($p['getattr'](self, 'main'), 'SERVER_SITE'),$add16='/movies/'),$add18=$p['str']($p['getattr']($p['getattr'](self, 'main'), 'mId'))), (typeof moviesControllerGET == "undefined"?$m['moviesControllerGET']:moviesControllerGET)($p['getattr'](self, 'main')));
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

			$p['getattr'](self, 'main')['eMessage'] = 'Error received from server. Unable to update movie.';
			self['main']['update']();
			return null;
		}
	, 1, [null,null,['self'],['text'],['code']]);
		$cls_definition['onError'] = $method;
		var $bases = new Array(pyjslib['object']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data['__setitem__']($item, $cls_definition[$item]); }
		return $p['_create_class']('recControllerGET', $p['tuple']($bases), $data);
	})();
	$m['recControllerPUT'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition['__module__'] = 'movies';
		$method = $pyjs__bind_method2('__init__', function(interface) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				interface = arguments[1];
			}

			self['main'] = interface;
			return null;
		}
	, 1, [null,null,['self'],['interface']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('onCompletion', function(text) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				text = arguments[1];
			}
			var data;
			data = $m['loads'](text);
			self['main']['getNewMovieRec']();
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

			$p['getattr'](self, 'main')['eMessage'] = 'Error received from server. Unable to update movie.';
			self['main']['update']();
			return null;
		}
	, 1, [null,null,['self'],['text'],['code']]);
		$cls_definition['onError'] = $method;
		var $bases = new Array(pyjslib['object']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data['__setitem__']($item, $cls_definition[$item]); }
		return $p['_create_class']('recControllerPUT', $p['tuple']($bases), $data);
	})();
	$m['moviesControllerGET'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition['__module__'] = 'movies';
		$method = $pyjs__bind_method2('__init__', function(interface) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				interface = arguments[1];
			}

			self['main'] = interface;
			return null;
		}
	, 1, [null,null,['self'],['interface']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('onCompletion', function(text) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				text = arguments[1];
			}
			var $add21,$add22,$add20,data,$add19;
			data = $m['loads'](text);
			$p['getattr'](self, 'main')['mTitle'] = data['__getitem__']('title');
			$p['getattr'](self, 'main')['mPoster'] = data['__getitem__']('img');
			$m['HTTPRequest']()['asyncGet']($p['__op_add']($add21=$p['__op_add']($add19=$p['getattr']($p['getattr'](self, 'main'), 'SERVER_SITE'),$add20='/ratings/'),$add22=$p['str']($p['getattr']($p['getattr'](self, 'main'), 'mId'))), (typeof ratingsControllerGET == "undefined"?$m['ratingsControllerGET']:ratingsControllerGET)($p['getattr'](self, 'main')));
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

			$p['getattr'](self, 'main')['eMessage'] = 'Error received from server. Unable to update movie.';
			self['main']['update']();
			return null;
		}
	, 1, [null,null,['self'],['text'],['code']]);
		$cls_definition['onError'] = $method;
		var $bases = new Array(pyjslib['object']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data['__setitem__']($item, $cls_definition[$item]); }
		return $p['_create_class']('moviesControllerGET', $p['tuple']($bases), $data);
	})();
	$m['ratingsControllerGET'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition['__module__'] = 'movies';
		$method = $pyjs__bind_method2('__init__', function(interface) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				interface = arguments[1];
			}

			self['main'] = interface;
			return null;
		}
	, 1, [null,null,['self'],['interface']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('onCompletion', function(text) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				text = arguments[1];
			}
			var data;
			data = $m['loads'](text);
			$p['getattr'](self, 'main')['mRating'] = data['__getitem__']('rating');
			self['main']['update']();
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

			$p['getattr'](self, 'main')['eMessage'] = 'Error received from server. Unable to update movie.';
			self['main']['update']();
			return null;
		}
	, 1, [null,null,['self'],['text'],['code']]);
		$cls_definition['onError'] = $method;
		var $bases = new Array(pyjslib['object']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data['__setitem__']($item, $cls_definition[$item]); }
		return $p['_create_class']('ratingsControllerGET', $p['tuple']($bases), $data);
	})();
	if ($p['bool']($p['op_eq']((typeof __name__ == "undefined"?$m['__name__']:__name__), '__main__'))) {
		$m['pyjd']['setup']('public/movies.html');
		$m['site'] = $m['movieInterface']();
		$m['RootPanel']()['add']($m['site']);
		$m['pyjd']['run']();
	}
	return this;
}; /* end movies */


/* end module: movies */


/*
PYJS_DEPS: ['pyjd', 'pyjamas.ui.RootPanel.RootPanel', 'pyjamas', 'pyjamas.ui', 'pyjamas.ui.RootPanel', 'pyjamas.ui.Label.Label', 'pyjamas.ui.Label', 'pyjamas.ui.Button.Button', 'pyjamas.ui.Button', 'pyjamas.ui.Grid.Grid', 'pyjamas.ui.Grid', 'pyjamas.ui.Image.Image', 'pyjamas.ui.Image', 'pyjamas.HTTPRequest.HTTPRequest', 'pyjamas.HTTPRequest', 'pyjamas.JSONService.loads', 'pyjamas.JSONService', 'pyjamas.JSONService.dumps', 'pygwt']
*/
