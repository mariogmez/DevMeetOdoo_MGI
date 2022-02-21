#!/bin/bash
echo "<odoo>"
echo "<data>"
while read line
do
    dni=$(echo $line | cut -d',' -f1)
    nombre=$(echo $line | cut -d',' -f2)
    year=$(echo $line | cut -d',' -f3)
    echo "<record id='$dni' model='school.student'>"
    echo "<field name='name'>$nombre</field>"
    echo "<field name='dni'>$dni</field>"
    echo "<field name='birth_year'>$year</field>"
    echo "<field name='tecnologia' ref='dev_meet.tecnologia1'></field>"
    echo "</record>"
done
echo "</data>"
echo "</odoo>"


