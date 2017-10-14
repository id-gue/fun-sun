<?php
/**
 * Created by PhpStorm.
 * User: janss
 * Date: 14.10.2017
 * Time: 17:45
 */

define (PYTHON_API,"/usr/bin/python sun.py --lat {lat} --lon {lon} --distance {distance}");

$file = file_get_contents('template.html');
$results="";
if (count($_POST)>0)
{
    var_dump($_POST);
    $lat=$_POST['lat'];
    $lon=$_POST['lon'];
    if (!is_numeric($lat)) exit;
    if (!is_numeric($lon)) exit;

    if (isset($_POST['distance1'])) $distance=100;
    else $distance=500;

    $toPython=PYTHON_API;
    $toPython = str_replace('{lat}',$lat,$toPython);
    $toPython = str_replace('{lon}',$lon,$toPython);
    $toPython = str_replace('{distance}',$distance,$toPython);
echo $toPython;
    exec(PYTHON_API,$result);
    $json= json_decode($result);
}

$file = str_replace('{results}',print_r($result,true),$file);

echo $file;

