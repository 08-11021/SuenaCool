stohtModule.service('servicesService', ['$q', '$http', function($q, $http) {
    this.createService = function(args) {
        return  $http({
          url: "/services/create",
          method: 'POST',
          params: args
        });
    };

    this.deleteService = function(args) {
        return  $http({
          url: "/services/delete",
          method: 'POST',
          params: args
        });
    };

    this.updateService = function(args) {
        return  $http({
          url: "/services/update",
          method: 'POST',
          params: args
        });
    };

    this.services = function(args) {
        return  $http({
          url: "/userServices",
          method: 'GET',
          params: args
        });
    };

}]);


