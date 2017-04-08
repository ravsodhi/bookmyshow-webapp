$(document).ready(
function renderSeats()
{
	//get audi type//
	//get data//
	var str_full="";
	for(var i=14;i >=0;i--)
	{
		row_no = String.fromCharCode(65 + i);
		var str_head = "<li class=\"row row-" + row_no +"\"><ol class=\"seats\" type=\"A\"><li class=\'seat\' style=\'color:white\'>"+ row_no +"</li>";
		var str_body="";
		for(var j=0;j<15;j++)
		{
			column_no = j+1;
			str_body += "<li class=\"seat\"><input type=\"checkbox\" id=\""+ row_no	+ column_no +"\" /><label for=\""+ row_no + column_no +"\">"/*+ row_no*/+ column_no +"</label></li>"
		}
		str_full += str_head + str_body +"</ol></li>";
		str_body="";
	}
		$("ol#seat-selector").html(str_full);
}
);