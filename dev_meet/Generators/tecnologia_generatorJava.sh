#!/bin/bash
echo "<odoo>"
echo "<data>"

    echo "<record id='tecnologia1' model='dev_meet.tecnologia'>"
    echo "<field name='name'>Java</field>"
    echo "<field name='pageoficial'>www.java.com</field>"
    echo "<field name='photo'>$(base64 imagenes/java.png)</field>"
    echo "</record>"

echo "</data>"
echo "</odoo>"


