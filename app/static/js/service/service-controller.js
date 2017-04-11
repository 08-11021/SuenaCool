//controlador de servicios
stohtModule.controller('servicesController',
   ['$scope', '$location', '$route', 'flash', 'servicesService','categoryService','loginService',
    function ($scope, $location, $route, flash, servicesService, categoryService, loginService) {
        $scope.view= "services";

        loginService.check({'securityLvl': 4}).then(function (object) {
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
        servicesService.services({}).then(function (object) {
            if(object.data['result'] != undefined){
              $scope.services = object.data['result'];
            }else{
                $scope.services = [];
            }
          });

        $location.search({});

        //Obtener Lista de servicios

        categoryService.categoriesTree({}).then(function (object) {
            if(object.data['result'] != undefined){
              $scope.categoryList = object.data['result'];
            }else{
                $scope.supercategories = [];
            }
          });

        //Solicitar servicio
        $scope.save = function(category) {
                servicesService.createService({name: $scope.name, category: category}).then(function (object) {
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

                servicesService.deleteService({id: id}).then(function (object) {
                if(object.data['error'] != undefined){
                  $scope.msg = object.data['error'];
                }else{
                    $scope.msg = object.data['reason'];

                    //Recargar lista de categorias
                    servicesService.services({}).then(function (object) {
                        if(object.data['result'] != undefined){
                          $scope.services = object.data['result'];
                        }else{
                            $scope.services = [];
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
