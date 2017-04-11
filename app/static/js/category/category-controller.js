//controlador de creacion de usuarios y lista de usuarios (administrador)
stohtModule.controller('categoriesController',
   ['$scope', '$location', '$route', 'flash', 'categoryService','loginService',
    function ($scope, $location, $route, flash, categoryService, loginService) {
        $scope.view= "categories";

        loginService.check({'securityLvl': 17}).then(function (object) {
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
        $location.search({});


        //Obtener Lista de categorias

        categoryService.categories({}).then(function (object) {
            if(object.data['result'] != undefined){
              $scope.supercategories = object.data['result'];
              $scope.category= $scope.supercategories[0];
                if($scope.category != undefined){
                  categoryService.getChildren({'parentCategory':$scope.category.id}).then(function (object) {
                    if(object.data['result'] != undefined){
                      $scope.categories = object.data['result'];
                    }else{
                        $scope.categories = [];
                    }
                  });
                    categoryService.breadcrumbs({id:$scope.category.id}).then(function (object) {
                        if(object.data['result'] != undefined){
                          $scope.crumbs = object.data['result'];
                            $scope.crumbs.pop();
                        }else{
                            $scope.crumbs = [];
                        }
                      });
                    }
            }else{
                $scope.supercategories = [];
            }
          });


        //Crear categoria
        $scope.save = function() {
                categoryService.createCategory({name: $scope.name}).then(function (object) {
                if (object.data['error'] != undefined) {
                        $scope.msg = object.data['error'];
                    } else {
                        if (object.data['status'] != 'failure') {
                            $scope.msg = object.data['reason'];
                            categoryService.categories({}).then(function (object) {
                                if(object.data['result'] != undefined){
                                  $scope.supercategories = object.data['result'];
                                }else{
                                    $scope.supercategories = [];
                                }
                              });
                        }else{
                            $scope.msg = object.data['reason'];
                        }
                    }
              });


      };

        $scope.saveSub = function() {

                categoryService.createCategory({name: $scope.subname, isSubCategory: true, parentCategory: $scope.category.id }).then(function (object) {
                if (object.data['error'] != undefined) {
                        $scope.msg = object.data['error'];
                    } else {
                        if (object.data['status'] != 'failure') {
                            $scope.msg = object.data['reason'];
                            categoryService.getChildren({'parentCategory':$scope.category.id}).then(function (object) {
                                if(object.data['result'] != undefined){
                                  $scope.categories = object.data['result'];
                                }else{
                                    $scope.categories = [];
                                }
                              });
                            categoryService.breadcrumbs({id:$scope.category.id}).then(function (object) {
                                if(object.data['result'] != undefined){
                                  $scope.crumbs = object.data['result'];
                                    $scope.crumbs.pop();
                                }else{
                                    $scope.crumbs = [];
                                }
                              });
                            $scope.subname = "";
                        }else{
                            $scope.msg = object.data['reason'];
                        }
                    }
              });


      };

        //Eliminar categoria
        $scope.delete = function(id) {

                categoryService.deleteCategory({id: id}).then(function (object) {
                if(object.data['error'] != undefined){
                  $scope.msg = object.data['error'];
                }else{
                    $scope.msg = object.data['reason'];

                    //Recargar lista de categorias
                    categoryService.categories({}).then(function (object) {
                        if(object.data['result'] != undefined){
                          $scope.supercategories = object.data['result'];
                        }else{
                            $scope.supercategories = [];
                        }
                      });

                }
              });


      };

        //Eliminar subcategoria
        $scope.deletesub = function(id) {

                categoryService.deleteCategory({id: id}).then(function (object) {
                //Recargar lista de subcategorias
                if(object.data['error'] != undefined){
                  $scope.msg = object.data['error'];
                }else{
                    $scope.msg = object.data['reason'];
                }
                categoryService.getChildren({'parentCategory':$scope.category.id}).then(function (object) {
                    if(object.data['result'] != undefined){
                      $scope.categories = object.data['result'];
                    }else{
                        $scope.categories = [];
                    }
                  });
                categoryService.breadcrumbs({id:$scope.category.id}).then(function (object) {
                    if(object.data['result'] != undefined){
                      $scope.crumbs = object.data['result'];
                        $scope.crumbs.pop();
                    }else{
                        $scope.crumbs = [];
                    }
                  });
              });
      };

        //actualizar categoria
        $scope.update = function() {
                categoryService.updateCategory({name: $scope.category.name, id: $scope.category.id, isSubcategory: $scope.category.isSubCategory, parentCategory: $scope.category.parent }).then(function (object) {
                if (object.data['error'] != undefined) {
                        $scope.msg = object.data['error'];
                    } else {
                        if (object.data['status'] != 'failure') {
                            $scope.msg = object.data['reason'];
                            categoryService.categories({}).then(function (object) {
                                if(object.data['result'] != undefined){
                                  $scope.supercategories = object.data['result'];
                                }else{
                                    $scope.supercategories = [];
                                }
                              });
                                categoryService.breadcrumbs({id:$scope.category.id}).then(function (object) {
                                if(object.data['result'] != undefined){
                                  $scope.crumbs = object.data['result'];
                                    $scope.crumbs.pop();
                                }else{
                                    $scope.crumbs = [];
                                }
                          });
                        }else{
                            $scope.msg = object.data['reason'];
                        }
                    }
              });


      };

        $scope.viewCategory = function(category) {
                $scope.category = category;
                categoryService.getChildren({'parentCategory':$scope.category.id}).then(function (object) {
                if(object.data['result'] != undefined){
                  $scope.categories = object.data['result'];
                }else{
                    $scope.categories = [];
                }
              });
                categoryService.breadcrumbs({id:$scope.category.id}).then(function (object) {
                    if(object.data['result'] != undefined){
                      $scope.crumbs = object.data['result'];
                        $scope.crumbs.pop();
                    }else{
                        $scope.crumbs = [];
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
