(function (document, window, $, Backbone, _){

	window.UTT = {
		Routers			: {},
		Views 			: {},
		Models			: {},
		Collections		: {},
		templateLoader 	: {}
	};

	UTT.Models.RestaurantModel = Backbone.Model.extend({		

		urlRoot : '/restaurants',

		initialize: function(){	
			console.log('sending data to:' + this.urlRoot);		
		},

		defaults: {			
			"id": null, 
			"restaurant_address": null, 
			"restaurant_image": null,
			"restaurant_name": null
	    }
	});

	UTT.Collections.RestaurantCollection = Backbone.Collection.extend({
		model 	: UTT.Models.RestaurantModel,
		url 	: '/restaurants'
	});

}(document, this, jQuery, Backbone, _));