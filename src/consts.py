class FileTypes:
    IMAGE: str = "image"
    VIDEO: str = "video"
    AUDIO: str = "audio"
    DOCUMENT: str = "document"
    ARCHIVE: str = "archive"
    EXECUTABLE: str = "executable"
    DATA: str = "data"
    DESIGN: str = "design"
    PRESENTATION: str = "presentation"
    SPREADSHEET: str = "spreadsheet"
    SYSTEM: str = "system"
    TORRENT: str = "torrent"
    OTHER: str = "other"


FILE_TYPE_EXTENSIONS_MAPPING: dict[str, tuple[str, ...]] = {
    FileTypes.IMAGE: (
        "jpg", "jpeg", "png", "gif", "bmp", "tiff", "tif",
        "svg", "webp", "heic", "heif", "ico", "raw", "cr2",
        "nef", "arw", "psd", "ai", "eps", "indd", "indt",
        "ico", "icns", "jp2", "j2k", "jpf", "jpx", "jpm",
        "dds", "exr", "hdr", "pbm", "pgm", "ppm", "pnm"
    ),
    FileTypes.VIDEO: (
        "mp4", "avi", "mov", "mkv", "wmv", "flv", "webm",
        "m4v", "mpg", "mpeg", "3gp", "m2ts", "ts", "mts",
        "vob", "ogv", "divx", "f4v", "rm", "rmvb", "asf",
        "avchd", "hevc", "h265", "h264", "prores", "dnxhd"
    ),
    FileTypes.AUDIO: (
        "mp3", "wav", "flac", "aac", "ogg", "wma", "m4a",
        "opus", "alac", "aiff", "pcm", "dsd", "dff", "dsf",
        "mid", "midi", "amr", "ac3", "mka", "tak", "ape",
        "cue", "m3u", "m3u8", "pls", "xspf"
    ),
    FileTypes.DOCUMENT: (
        "pdf", "doc", "docx", "txt", "rtf", "odt", "pages",
        "xls", "xlsx", "csv", "ods", "numbers", "ppt", "pptx",
        "odp", "key", "md", "tex", "epub", "mobi", "fb2",
        "djvu", "djv", "oxps", "xps", "chm", "hlp", "lit"
    ),
    FileTypes.ARCHIVE: (
        "zip", "rar", "7z", "tar", "gz", "bz2", "xz", "lz",
        "lzma", "z", "lzh", "arj", "cab", "iso", "dmg",
        "pkg", "rpm", "deb", "cpio", "zst", "lz4", "br",
        "tar.gz", "tar.bz2", "tar.xz", "tgz", "tbz2", "txz"
    ),
    FileTypes.EXECUTABLE: (
        "exe", "msi", "bat", "cmd", "sh", "bash", "ps1",
        "app", "dmg", "pkg", "deb", "rpm", "apk", "jar",
        "ipa", "xap", "msix", "appx", "vb", "vbs", "js",
        "py", "php", "pl", "rb", "go", "java", "class"
    ),
    FileTypes.DATA: (
        "json", "xml", "yaml", "yml", "ini", "cfg", "conf",
        "toml", "env", "sql", "db", "sqlite", "sqlite3",
        "mdb", "accdb", "dbf", "mdf", "ldf", "log", "dat",
        "csv", "tsv", "ods", "xlsx", "parquet", "avro",
        "orc", "feather", "hdf5", "h5", "nc", "mat", "sav"
    ),
    FileTypes.DESIGN: (
        "ai", "eps", "psd", "xd", "fig", "sketch", "afdesign",
        "afphoto", "afpub", "cdr", "dwg", "dxf", "svg",
        "indd", "indt", "idml", "qxp", "pub", "vsd", "vsdx"
    ),
    FileTypes.PRESENTATION: (
        "ppt", "pptx", "odp", "key", "pps", "ppsx", "pdf",
        "swf", "fla", "flv", "prezi", "gslides"
    ),
    FileTypes.SPREADSHEET: (
        "xls", "xlsx", "xlsm", "xlsb", "ods", "csv", "tsv",
        "numbers", "gnumeric", "dif", "slk", "qpw", "wk1"
    ),
    FileTypes.SYSTEM: (
        "dll", "sys", "drv", "vxd", "ocx", "cpl", "mui",
        "msc", "scr", "theme", "deskthemepack", "diagcab",
        "diagpkg", "edb", "reg", "regtrans-ms", "blf"
    ),
    FileTypes.TORRENT: (
        "torrent", "magnet"
    )
}
