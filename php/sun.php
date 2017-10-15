<?php
/**
 * Created by PhpStorm.
 * User: janss
 * Date: 14.10.2017
 * Time: 17:45
 */
require_once 'Poi.php';
//>test.json 2>&1
define('PYTHON_API', "/usr/bin/python3 /var/www/funsun/play.py --lat {lat} --lon {lon} --distance {distance}");
error_reporting(E_ALL);
ini_set('display_errors', true);
$file = file_get_contents('template.html');

$formattedResults = "";
if (count($_POST) > 0) {
    //var_dump($_POST);
    $lat = $_POST['lat'];
    $lon = $_POST['lon'];
    if (!is_numeric($lat)) exit;
    if (!is_numeric($lon)) exit;

    if (isset($_POST['distance1'])) $distance = 10;
    else $distance = 50;

    $toPython = PYTHON_API;
    $toPython = str_replace('{lat}', $lat, $toPython);
    $toPython = str_replace('{lon}', $lon, $toPython);
    $toPython = str_replace('{distance}', $distance, $toPython);
/*
    echo "<br>".$toPython . "<br>";
    $result = exec($toPython, $returnState);
  */
    //temporary
    $result = file_get_contents("/var/www/funsun/output.json");

    if (isset($result)) {
        $json = json_decode($result, true);
        //var_dump($json);
    }

    $pois = array();

    //Put JSON into Object
    foreach ($json as $res) {
        //echo "<hr>";
        //print_r($res);
        $poi = new Poi();
        $poi->title = $res['title'];
        $poi->lat = $res['location']['latitude'];
        $poi->lon = $res['location']['longitude'];
        $pois[] = $poi;
    }

    //create a nice list
    $formattedResults = "<ul>";
    foreach ($pois as $poi) {
        $formattedResults .= "<li>" . $poi->title . "</li>";
    }

    $formattedResults .= "</ul>";
}

//output the template
$file = str_replace('{results}', $formattedResults, $file);

echo $file;

