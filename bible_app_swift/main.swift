import bible_reading

@main 
struct App
{
    static func  main()
    {

        do {
            let bibleText = try readBible(fName: BIBLE)
            print(bibleText)
        } 
        catch {
            print("Error reading the Bible: \(error)")
        }

        
    }

}