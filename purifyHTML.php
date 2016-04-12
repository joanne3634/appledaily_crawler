<?php
require_once './simple_html_dom.php';

$aidsDone = array();
$aidsPending = array();

if (file_exists("./appledaily/profiles/overall.csv")) {
	$fileDone = fopen("./appledaily/profiles/overall.csv", "r");
	while (!feof($fileDone)) {
		$lines = fgetcsv($fileDone);
		foreach ($lines as $key => $value) {
			if ($key == 0) {
				$aidsDone[$value] = 1;
			} else {
				break;
			}
		}
	}
	array_unique($aidsDone);
	fclose($fileDone);
}
if (file_exists("./appledaily/profiles/未結案/overall.csv")) {
	$filePending = fopen("./appledaily/profiles/未結案/overall.csv", "r");
	while (!feof($filePending)) {
		$lines = fgetcsv($filePending);
		foreach ($lines as $key => $value) {
			if ($key == 0) {
				$aidsPending[$value] = 1;
			} else {
				break;
			}
		}
	}
	array_unique($aidsPending);
	fclose($filePending);
}

transformArticle($aidsDone, '');
transformArticle($aidsPending);

function transformArticle($aids, $pending = '未結案/') {
	foreach ($aids as $lid => $value) {
		if ($lid) {
			$dirty_html = file_get_html("./appledaily/profiles/{$pending}$lid[4]/{$lid}/{$lid}_origin.htm");

			$clean_html = str_get_html('<html lang="zh-TW"><head></head><body></body>');

			$head = $dirty_html->find('head', 0);
			foreach ($head->find('script') as $element) {
				$element->outertext = '';
			}

			$clean_html->find('head', 0)->innertext = $head;

			$article = $dirty_html->find('article', 1);
			foreach ($article->find('div#articlelast,div#articlelast2,a[_moz_dirty],a.chari_banner,head script,label,select,header div,style,div.aml_like,div.gggs div, div.gggs a,span,div.articulum div, div.articulum iframe,') as $element) {
				$element->outertext = '';
			}

			$clean_html->find('body', 0)->innertext = $article;
			$clean_html->save("./appledaily/profiles/{$pending}$lid[4]/{$lid}/{$lid}.htm");
		}
	}
}

?>
