

(function(window){


	// var bad_array = new Array(3),
	// good_array = [3];

	// console.log(bad_array.length, good_array.length);

	// var obj = new Object(),
	// obj2 = {};


	var object_lit = {
		"person": "nick",
		"purpose" : "student",
		"getPerson" : function(){
			return this.person;
		}
	};

	// console.log(object_lit.getPerson())
	var g_v = "Global";

	var Person = function(){
		console.log("inside Person "+ g_v);
		var p_v = "Private Variable";
		this.name = "Nick";
		this.purpose = "student";
		// this.getPerson = function(){
		// 	console.log("Inside getperson"+p_v);
		// 	return this.name;
		// };
	};

	Person.prototype.getPerson = function(){
		return this.name;
	};

	// var p = new Person();
	// console.log(p.getPerson());

	


})(window);