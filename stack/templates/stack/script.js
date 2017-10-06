function showAndHide(first, second)
{
  show(first);
  hide(second);
}

function hide(e)
{
  if(e.style.display == '')
     e.style.display = 'none';
}

function show(e)
{
  if(e.style.display == 'none')
     e.style.display = '';
}
