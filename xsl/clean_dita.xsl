<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:ditaarch="http://dita.oasis-open.org/architecture/2005/"
    version="2.0">
    <xsl:output method="xml" omit-xml-declaration="no" indent="yes"/>
    <xsl:strip-space elements="*"/>

    <!-- this template adds the doctype back in for the appropriate dita topic type -->

    <xsl:template match="/">
        <xsl:choose>
            <xsl:when test="name(node()[1]) = 'bookmap'">
                <xsl:text disable-output-escaping="yes">
&lt;!DOCTYPE bookmap PUBLIC "-//OASIS//DTD DITA 1.2 BookMap//EN" "bookmap.dtd"&gt;
</xsl:text>
            </xsl:when>
            <xsl:when test="name(node()[1]) = 'map'">
                <xsl:text disable-output-escaping="yes">
&lt;!DOCTYPE map PUBLIC "-//OASIS//DTD DITA Map//EN" "map.dtd"&gt;
</xsl:text>
            </xsl:when>
            <xsl:when test="name(node()[1]) = 'topic'">
                <xsl:text disable-output-escaping="yes">
&lt;!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd"&gt;
</xsl:text>
            </xsl:when>
            <xsl:when test="name(node()[1]) = 'concept'">
                <xsl:text disable-output-escaping="yes">
&lt;!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN" "concept.dtd"&gt;
</xsl:text>
            </xsl:when>
            <xsl:when test="name(node()[1]) = 'task'">
                <xsl:text disable-output-escaping="yes">
&lt;!DOCTYPE task PUBLIC "-//OASIS//DTD DITA Task//EN" "task.dtd"&gt;
</xsl:text>
            </xsl:when>
            <xsl:when test="name(node()[1]) = 'reference'">
                <xsl:text disable-output-escaping="yes">
&lt;!DOCTYPE reference PUBLIC "-//OASIS//DTD DITA Reference//EN" "reference.dtd"&gt;
</xsl:text>
            </xsl:when>
        </xsl:choose>
        <xsl:apply-templates select="node()"/>
    </xsl:template>

    <!-- This is the identity transform - it copies the entire xml file, this allows you to do further transforms -->

    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>
    
 <!-- This next bit removes namespaces. how bout that -->   
    
    <xsl:template match="*">
        <xsl:element name="{local-name()}">
            <xsl:apply-templates select="@*|node()"/>
        </xsl:element>
    </xsl:template>
    
    <xsl:template match="@*">
        <xsl:attribute name="{local-name()}">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    
    <!-- This find all instances of the topicmeta node and deletes it and all child nodes. The following templates clean out the left over domain and class and namespace attributes -->

    <xsl:template match="topicmeta"/>
    <xsl:template match="@domains"/>
    <xsl:template match="@class"/>
    <xsl:template match="@outputclass"/>
    <xsl:template match="@xtrc"/>
    <xsl:template match="@xtrf"/>
    <xsl:template match="@lang"/>
    <xsl:template match="@ditaarch:DITAArchVersion"/>

</xsl:stylesheet>
