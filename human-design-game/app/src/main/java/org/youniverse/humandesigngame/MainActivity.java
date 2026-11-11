package org.youniverse.humandesigngame;
import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.webkit.WebResourceRequest;
import android.net.Uri;
import android.content.Intent;
public class MainActivity extends Activity {
 @Override public void onCreate(Bundle state){super.onCreate(state); WebView view=new WebView(this);view.getSettings().setJavaScriptEnabled(true);view.getSettings().setDomStorageEnabled(true);view.getSettings().setAllowFileAccess(true);view.setWebViewClient(new WebViewClient(){@Override public boolean shouldOverrideUrlLoading(WebView v, WebResourceRequest request){Uri u=request.getUrl(); if("file".equals(u.getScheme()))return false; if("http".equals(u.getScheme())||"https".equals(u.getScheme())){startActivity(new Intent(Intent.ACTION_VIEW,u));return true;}return true;}});setContentView(view);view.loadUrl("file:///android_asset/index.html");}
}
