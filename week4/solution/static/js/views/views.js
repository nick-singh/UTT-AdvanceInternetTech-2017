(function (document, window, $, Backbone, _){


	UTT.Views.Home = Backbone.View.extend({

		className : "row",

		initialize : function(){
			this.render();
		},

		collection : new UTT.Collections.RestaurantCollection(),

		render : function(){		
			$(this.el).html(this.template());				
			restaurantBody = this.$el.find("#reviewBody")
			this.collection.fetch({
				success : function(model, response){
					console.log(response)
					$.each(response.restaurants, function(index, data){
						$(restaurantBody).append(new UTT.Views.Restaurant({model:data}).el);
					})
				},
				error: function(model, response){
					console.log(response);
				}
			});
			return this;
		},

		events : {			
			"submit #resturant-form"	: "addRestaurant"			
		},

		addRestaurant : function(){
			var data =  this.getFormData(),
			that = this,
			resturant = new UTT.Models.RestaurantModel();
			console.log(data);
			if(!_.isEmpty(data)){
				resturant.save(data,{
					success:function(model, response){							
						that.collection.add(response);
					  	that.render();
					},
					error : function(model, response){						
						window.aelrt("Error Processing")								
					}
				});	
			}else{
				window.alert("Empty form");
			}
			return false;
		},

		getFormData : function(){			
			var data = {},
			form = this.$el.find("#resturant-form"),
			viewArr = form.serializeArray(),
			valid = true;			

			$.each(viewArr, function(i,d){
				data[viewArr[i].name] = viewArr[i].value;
				if(viewArr[i].value === "") valid = false;
			});		
			if(valid){
				return data;
			}else{
				return {};
			}
		}

	});


	UTT.Views.Restaurant = Backbone.View.extend({

		className : "row restaurantBody",

		initialize : function(){
			this.render();
		},

		render : function(){		
			$(this.el).html(this.template(this.model));	
			return this;
		}

	});


	
}(document, this, jQuery, Backbone, _));