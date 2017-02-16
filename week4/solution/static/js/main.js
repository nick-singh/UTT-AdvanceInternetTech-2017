(function (document, window, $, Backbone, _){
	

	UTT.Routers.AppRouter = Backbone.Router.extend({

		routes: {
			"" 	: "home"
		},

		initialize : function(){
			console.log("initialize");					

		},

		home : function(){	

				
			this.home = new UTT.Views.Home();				
			$("#content").html(this.home.el);
			// this.authen.selectMenuItem('applications');				
		}

	});

	UTT.templateLoader.load(["Home", "Restaurant"],function () {      
		$(document).ready(function(){
			app = new UTT.Routers.AppRouter();
			Backbone.history.start();
		});
	});


}(document, this, jQuery, Backbone, _));
