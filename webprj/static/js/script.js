var contentname = Array();
var novelname = Array();
var contentnumber = Array();
var novelnumber = Array();

var mydata;
d3.csv("https://raw.githubusercontent.com/kimnamheeee/BOJ/main/sherlock.csv", // 배열에 데이터 담기
function(error, data) {
    mydata = data;
    for(var i=0; i<mydata.length; i++) {
        contentname.push(mydata[i]['contentname']);
        novelname.push(mydata[i]['novelname']);
        contentnumber.push(mydata[i]['contentnumber']);
        novelnumber.push(mydata[i]['novelnumber']);
    }

    d3.selectAll(".listInner") // listInner 안에 span으로 데이터 넣기
      .data(novelname)
      .append("span")
      .text(function(d) {return d;})
      .classed("novel", true);

    d3.selectAll(".listInner")
      .data(contentname)
      .append("span")
      .text(function(d) {return d;})
      .classed("content", true);
});

for (var i =0; i < 56; i ++){ // listInner div 생성하기
    var listBox = document.getElementById('listBox')
    var div = document.createElement('div');
    div.className = "listInner";
    listBox.appendChild(div);
};

function filter() { // 검색기능 구현
    let search = document.getElementById("search").value.toLowerCase();
    let listInner = document.getElementsByClassName("listInner");

    for(let i = 0; i < listInner.length; i++) {
        content = listInner[i].getElementsByClassName("content");
        novel = listInner[i].getElementsByClassName("novel");
        if (content[0].innerHTML.toLowerCase().indexOf(search) != -1 ||
            novel[0].innerHTML.toLowerCase().indexOf(search) != -1
        ) {
            listInner[i].style.display = "flex"
        } else {
            listInner[i].style.display = "none"
        };
    };
};

// eventListeners
var startbutton = document.getElementById("startbutton");
var changepart = document.getElementById("subtitle");
var title = document.getElementById("webtitle");
var main = document.getElementById("main");
var search = document.getElementById("search")

startbutton.addEventListener("click", startweb);

function startweb() {
    changepart.style.display = 'none';
    title.classList.add("go");
}

title.addEventListener("transitionend", appear);
search.addEventListener("click", searchappear);

function appear () {
    main.style.visibility = "visible";
}

function searchappear() {
    if (listBox.style.visibility == "hidden"){
        listBox.style.visibility = "visible";
    } else {
        listBox.style.visibility = "hidden";
    }
}
