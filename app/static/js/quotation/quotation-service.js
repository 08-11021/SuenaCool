stohtModule.service('requestsService', ['$q', '$http', function($q, $http) {
    this.requests = function(args) {
        return  $http({
            url: "/quotations",
            method: 'GET',
            params: args
        });
    };

}]);
