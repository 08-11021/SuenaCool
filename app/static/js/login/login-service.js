stohtModule.service('loginService', ['$q', '$http',function($q, $http) {
this.authenticate = function(args) {
        return  $http({
          url: "user/authenticate",
          method: 'POST',
          params: args
        });
    };

   this.check = function(args){

       return  $http({
          url: "user/check",
          method: 'GET',
          params: args
        });
   };
    
    this.logout = function(args){

       return  $http({
          url: "user/logout",
          method: 'GET',
          params: args
        });
   };

}]);
