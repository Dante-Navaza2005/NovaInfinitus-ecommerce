/*
the url is a instance of the URL class
document.URL gets the current URL
*/
var url = new URL(document.URL);
var items = document.getElementsByClassName("item-order"); //returns a list of the three href elements

for (i = 0; i < items.length; i++)
{
    url.searchParams.set("order", items[i].value); //(name, value)
    items[i].value = url.href;
};

