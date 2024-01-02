let BIBLE: String = "bible_app_swift/data_files/kjv_strongs.txt";


func readBible(fName: String) throws -> String {
    let file = URL(fileURLWithPath: fName)
    let bibleData = try String(contentsOf: file, encoding: .utf8)
    return bibleData
}


func cleanBible(bible: String) -> [String] {
    let punctuationSet = Set(".,?!:;\"'()[]{}-_")
    let cleanedBible = bible
        .filter { !punctuationSet.contains($0) }
        .lowercased()
        .components(separatedBy: .whitespacesAndNewlines)
        .filter { !$0.isEmpty }
    return cleanedBible
}
