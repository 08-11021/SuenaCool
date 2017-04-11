//controlador de servicios
stohtModule.controller('suscriptionsController',
   ['$scope', '$location', '$route', 'flash', 'suscriptionsService','categoryService','loginService',
    function ($scope, $location, $route, flash, suscriptionsService, categoryService, loginService) {
        $scope.view= "suscriptions";

        loginService.check({'securityLvl': 2}).then(function (object) {
                if (object.data['redirect'] == undefined) {
                    $scope.actorName = object.data['actorName'];
                    $scope.actorRol = object.data['actorRol'];

                    $scope.isAdmin= ($scope.actorRol & 1) !== 0;
                    $scope.isOperator= ($scope.actorRol & 2) !== 0;
                    $scope.isClient = ($scope.actorRol & 4) !==0;
                    $scope.isManager = ($scope.actorRol & 16) !==0;
                } else {
                    $location.path(object.data['redirect']);
                }
            });
        $scope.msg = "";
        suscriptionsService.suscriptions({}).then(function (object) {
            if(object.data['result'] != undefined){
              $scope.suscriptions = object.data['result'];
            }else{
                $scope.suscriptions = [];
            }
          });

        $location.search({});

        //Obtener Lista de categorias

        categoryService.categoriesTree({}).then(function (object) {
            if(object.data['result'] != undefined){
              $scope.categoryList = object.data['result'];
            }else{
                $scope.supercategories = [];
            }
          });

        //Solicitar suscripcion
        $scope.save = function(category) {
                suscriptionsService.createSuscription({category: category}).then(function (object) {
                if (object.data['error'] != undefined) {
                        $scope.msg = object.data['error'];
                    } else {
                        if (object.data['status'] != 'failure') {
                            $scope.msg = object.data['reason'];
                            $route.reload();
                        }else{
                            $scope.msg = object.data['reason'];

                        }
                    }
              });


      };

        //Eliminar solicitud
        $scope.delete = function(id) {

                suscriptionsService.deleteSuscription({id: id}).then(function (object) {
                if(object.data['error'] != undefined){
                  $scope.msg = object.data['error'];
                }else{
                    $scope.msg = object.data['reason'];

                    //Recargar lista de suscripciones
                    suscriptionsService.suscriptions({}).then(function (object) {
                        if(object.data['result'] != undefined){
                          $scope.suscriptions = object.data['result'];
                        }else{
                            $scope.suscriptions = [];
                        }
                      });

                }
              });


      };

        //cierre de sesion
        $scope.logout = function() {
            loginService.logout().then(function(object){
                $location.path('/');
            });

        };
    }]);
