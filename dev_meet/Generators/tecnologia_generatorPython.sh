#!/bin/bash
echo "<odoo>"
echo "<data>"

    echo "<record id='tecnologia2' model='dev_meet.tecnologia'>"
    echo "<field name='name'>Python</field>"
    echo "<field name='pageoficial'>www.python.com</field>"
    echo "<field name='photo'>$(base64 imagenes/python.png)</field>"
    echo "</record>"

echo "</data>"
echo "</odoo>"


