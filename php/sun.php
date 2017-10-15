<?php
/**
 * Created by PhpStorm.
 * User: Inna Janssen
 * Date: 14.10.2017
 * Time: 17:45
 *
 * This is just a very hacky demonstration of how we can use some APIs and show
 * them in a map.
 * This is a demo for the hackathon 2017 in Berlin.
 *
 * The API-Calls are happening in a python-script, so we call the python script
 * via php-exec :-)
 * TODOs: put everything into classes and so on...
 */
require_once 'Poi.php';

//these paths have to be configured!
define('PYTHON_API', "/usr/bin/python3 /var/www/funsun/play.py --lat {lat} --lon {lon} --distance {distance}");

//call API or just load a json file?
define('DO_REAL',true);

//for debugging purposes:
error_reporting(E_ALL);
ini_set('display_errors', true);

//this is the most simple Template-Engine
$file = file_get_contents('template.html');

$formattedResults = "";
$javaScriptMarkers="";

//do the api-CALLS when the User presses a Button
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


    if (DO_REAL) {
        //echo "<br>" . $toPython . "<br>";
        $result = exec($toPython, $returnState);
    }
    //temporary
    else $result = file_get_contents("/var/www/funsun/locmuseum200.json");

    if (isset($result)) {
        $json = json_decode($result, true);
        //var_dump($json);
    }

    $pois = array();

    //Put JSON into Object
    $i=0;
    foreach ($json as $res) {
        //echo "<hr>";
        //print_r($res);
        $poi = new Poi();
        $poi->title = $res['title'];
        $poi->lat = $res['location']['latitude'];
        $poi->lon = $res['location']['longitude'];
        $poi->photoUrl=str_replace('http://','https://',$res['main_image']);
        $pois[] = $poi;
        $i++;
        if ($i>10) break;
    }

    //create a nice list
    $formattedResults = "<h2>Found:</h2><ul>";
    foreach ($pois as $poi) {
        $formattedResults .= "<li>" . $poi->title
           //  . "<br><img src='".$poi->photoUrl."'>"
             ."</li>";
        $javaScriptMarkers .="L.marker([".$poi->lat.", ".$poi->lon."],{color: 'red'}).\n";
        $javaScriptMarkers .="bindPopup(\"<img src='".
            $poi->photoUrl."' style='width:200px'><div class='imageunderline'>".
            $poi->title."</div>\").addTo(mymap);";
    }

    $formattedResults .= "</ul>";
}

//output the template
$file = str_replace('{list}', $formattedResults, $file);
$file = str_replace('{results}', "", $file);
$file = str_replace('{markers}', $javaScriptMarkers, $file);

echo $file;

