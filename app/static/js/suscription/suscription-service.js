stohtModule.service('suscriptionsService', ['$q', '$http', function($q, $http) {
    this.createSuscription = function(args) {
        return  $http({
          url: "/suscriptions/create",
          method: 'POST',
          params: args
        });
    };

    this.deleteSuscription = function(args) {
        return  $http({
          url: "/suscriptions/delete",
          method: 'POST',
          params: args
        });
    };

    this.updateSuscription = function(args) {
        return  $http({
          url: "/suscriptions/update",
          method: 'POST',
          params: args
        });
    };

    this.suscriptions = function(args) {
        return  $http({
          url: "/userSuscriptions",
          method: 'GET',
          params: args
        });
    };

}]);


