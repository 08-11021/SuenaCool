stohtModule.service('signupService', ['$q', '$http',function($q, $http) {
this.signup = function(args) {
        return  $http({
          url: "user/create",
          method: 'POST',
          params: args
        });
    };

}]);
