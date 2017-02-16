(function(window){
'user strict';

var fullName = "";


var Person  = function(){
	this.firstName = "";
	this.lastName = "";
	this.sex = "";

	var country = "NoWhere";
	this.getCountry = function(){ return country; };
	this.setCountry = function(c){ country = c; };
};


Person.prototype.setName = function(fullName){
	var name = fullName.split(" ");// Delimiter 
	if(name.length === 2){
		this.firstName = name[0];
		this.lastName = name[1];
	}
	else window.console.log("Error in setting name");
};


Person.prototype.setDetails = function(details){
	if(details.firstName){
		this.firstName = details.firstName;
	}
	if (details.lastName) {
		this.lastName = details.lastName;
	}
	if(details.sex){
		this.sex = details.sex;
	}
	if (details.country) {
		this.setCountry(details.country);
	}
};


Person.prototype.printPerson = function(){
	var str = "";
	str+="First Name: "+this.firstName;
	str+=" Last Name: "+this.lastName;
	str+=" Sex: "+this.sex;
	str+=" Country: "+this.getCountry();
	return str;
};
//First Example
var p = new Person();
fullName = "Nicholas Chamansingh";
p.setName(fullName);
window.console.log(JSON.stringify(p));

var details = {
	"firstName": "John",
	"lastName": "Doe",
	"sex": "male",
	"country": "Trinidad"
};


//Second Example
p2 = new Person()
p2.setDetails(details);

console.log(p2.printPerson());
// console.log(JSON.stringify(Person()));


var PersonManager = function(){
	this.persons = [];
};

PersonManager.prototype.addPerson = function(person){
	if(person instanceof Person){
		window.console.log("Entering person: "+person.printPerson());
		var id;
		id = this.persons.length;
		this.persons.push(person);
		return id;
	}
	else{
		window.console.log("No Person Entered");
	}
};


PersonManager.prototype.removePersonById = function(indx){
	if(indx >= 0 && indx < this.persons.length){ // check is valid index
		delete this.persons[indx];
		return true;
	}
	return false;
};

pManager = new PersonManager();
pManager.addPerson(p);
pManager.addPerson(p2);

window.console.log(pManager.persons.length);
pManager.removePersonById(0);
window.console.log(pManager.persons.length);


})(window);