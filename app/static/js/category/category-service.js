stohtModule.service('categoryService', ['$q', '$http', function($q, $http) {
    this.createCategory = function(args) {
        return  $http({
          url: "/categories/create",
          method: 'POST',
          params: args
        });
    };

    this.deleteCategory = function(args) {
        return  $http({
          url: "/categories/delete",
          method: 'POST',
          params: args
        });
    };

    this.updateCategory = function(args) {
        return  $http({
          url: "/categories/update",
          method: 'POST',
          params: args
        });
    };

    this.categories = function(args) {
        return  $http({
          url: "categories",
          method: 'GET',
          params: args
        });
    };

    this.getChildren = function(args) {
        return  $http({
          url: "/categories/children",
          method: 'GET',
          params: args
        });
    };

    this.breadcrumbs = function(args) {
        return  $http({
          url: "/categories/breadcrumbs",
          method: 'GET',
          params: args
        });
    };

    this.categoriesTree = function(args) {
        return  $http({
          url: "/categories/tree",
          method: 'GET',
          params: args
        });
    };


}]);


