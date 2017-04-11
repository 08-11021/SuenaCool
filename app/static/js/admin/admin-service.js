stohtModule.service('adminService', ['$q', '$http', function($q, $http) {
    this.createUser = function(args) {
        return  $http({
          url: "user/create",
          method: 'POST',
          params: args
        });
    };

    this.deleteUser = function(args) {
        return  $http({
          url: "user/delete",
          method: 'POST',
          params: args
        });
    };

    this.updateUser = function(args) {
        return  $http({
          url: "user/update",
          method: 'PUT',
          params: args
        });
    };

    this.users = function(args) {
        return  $http({
          url: "users",
          method: 'GET',
          params: args
        });
    };

    this.getUser = function(args) {
        return  $http({
          url: "user",
          method: 'GET',
          params: args
        });
    };

}]);


