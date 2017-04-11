stohtModule.service('requestsService', ['$q', '$http', function($q, $http) {
    this.requests = function(args) {
        return  $http({
          url: "/requests",
          method: 'GET',
          params: args
        });
    };

}]);


