# Web Crawler
This project aims to record specified images, videos, or video streams. In further stages, it will be extended
by multiple algorithms based on data mining and artificial intelligence.

<!--- 
## Network Traffic Capture )

Usually, in order to capture video streams from a webpage, we need to monitor the network traffic.

* [BrowserMob-proxy](https://bmp.lightbody.net/)

> is based on technology developed in the Selenium open source project and a commercial load testing and monitoring 
    service originally called BrowserMob. Through pip command `pip install browsermob-proxy`, we can import its 
    module into python. However, BrowserMob-proxy requires a binary file called `browsermob-proxy.bat`, which only 
    support Linux system.) 
-->

## Video Stream
Currently, video stream could be in following formats: M3U8(TS) and MPD(M4S).


### M3U8(TS)
M3U (MP3 URL or Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator in full) is a computer file 
format for a multimedia playlist. M3U was originally developed by Fraunhofer for use with their Winplay3 software, 
but numerous media players and software applications now support the format. An M3U file is a plain text file that 
specifies the locations of one or more media files. The file is saved with the "m3u" filename extension if the text is 
encoded in the local system's default non-Unicode encoding (e.g., a Windows codepage), or with the "m3u8" extension if 
the text is UTF-8 encoded. <sup>[1](https://en.wikipedia.org/wiki/M3U)</sup>

M3U8 file itself does not contain video data, but a list of links which point multiple video slices. These slices are 
saved in format TS (MPEG-2 Transport Stream). 


## HTML

* `<figure>` vs `<img>`

> The `<img>` tag creates a holding space for the referenced image.  
> While the content of the `<figure>` element is related to the main flow, its position is independent of the main flow, and if removed it should not affect the flow of the document

* Second item
* Third item
* Fourth item

## Selenium
Selenium is a portable framework for testing web applications. Selenium provides a playback (formerly also recording) 
tool for authoring functional tests without the need to learn a test scripting language (Selenium IDE).  
It also provides a test domain-specific language (Selenese) to write tests in a number of popular programming 
languages, including C#, Groovy, Java, Perl, PHP, Python, Ruby and Scala. The tests can then run against most 
modern web browsers. Selenium deploys on Windows, Linux, and macOS platforms. It is open-source software, released 
under the Apache 2.0 license: web developers can download and use it without charge. <sup>[2](https://de.wikipedia.org/wiki/Selenium)</sup>

With Selenium, we can implement automatic interactions with webpages.

### Key Table of Selenium
Package `from selenium import webdriver`

| Command | Meaning |
|:---|:----------------------|
|`element.send_keys(Keys.ENTER)`        | send `enter` or click|
|`element.send_keys(Keys.CONTROL,'a')`  | send `Ctrl+A` = select all|
|`element.send_keys(Keys.ARROW_DOWN)`   | press `Down` key  |
|`element.send_keys("some text")`       | send a string |
|`elem.send_keys("Administrator" + Keys.RETURN)` | send a string and press `enter` |
|`element.send_keys(Keys.PageDown)`     | scroll down the page |
|`element.send_keys(Keys.SPACE)`        | send space = select if the element is radio buttom or checkbox |


### Mouse Actions
Package `from selenium.webdriver.common.action_chains import ActionChains`

| Command | Meaning |
|:---|:---|
|`action = ActionChains(driver).move_to_element(element)`| move the mouse to an element  |
|`action.context_click(element)`| right click on the element  |
|`action.send_keys('v')`        | press `v` to perform the shortcut |
|`action.perform()`             | perform the mouse action |



### Other Functions
Package `from selenium.webdriver.common.keys import Keys`

| Command | Meaning |
|:---|:---|
|`element.click()`| click element |
|`element = driver.find_element_by_name("q")`| find element by name|
|`element = driver.find_element_by_id("id")`| find element by id|
|`element = driver.find_element_by_xpath('//input[@value="rv2"]')`| find element by xpath|
|`element = driver.find_element_by_link_text("linktext")`| find element by linked text (not link)|
|`element = driver.find_element_by_partial_link_text("link_text")`| find element by particial linked text (not link)|
|`element = driver.find_element_by_tag_name("tag_name")`| find element by tag name|
|`element = driver.find_element_by_class_name("class_name")`| find element by class name|
|`element = driver.find_element_by_css_selector("h1.importane")`| find element by css selector|
|`element.is_selected()`|check whether the element is selected|
|`driver.refresh()`| refresh the page |
|`element.submit()`| submit contents (e.g. string) = click if element is a form |
|`element.clear()`| clear the content of the a input field |

With `driver.find_elements_by ...`, we can get a list of satisfactory elements.

### Configurations

* Page Load Strategy
> With the configuration of page load strategy, we can define whether the following command always wait for full load.

``` 
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    caps = DesiredCapabilities().FIREFOX
    caps["pageLoadStrategy"] = "eager"
    browser = webdriver.Firefox(capabilities=caps)
```
