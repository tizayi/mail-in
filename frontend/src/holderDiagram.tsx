import "./App.css"
import {  Card, CardBody, IconButton, HStack, Center, Stack, Popover, PopoverTrigger, PopoverContent, PopoverCloseButton, PopoverHeader, PopoverBody, PopoverArrow} from '@chakra-ui/react'
import { CheckCircleIcon } from '@chakra-ui/icons'
import { BatchSampleInfo, HplcSampleInfo } from "./sampleInfo"
import {HolderMode} from "./types"

export default function HolderDiagram(props: {mode:HolderMode}) {
    const positions = [1,2,3,4,5,6,7,8,9,]

    return (
      <>
      <Card>
          <CardBody>
          <HStack>
            {positions.map((position) => (
                <Stack>
                    <Center>{position}</Center>
                    <Popover placement='right'>
                    <PopoverTrigger>
                        <IconButton
                        variant='outline'
                        colorScheme='teal'
                        aria-label='Send email'
                        icon={<CheckCircleIcon />}
                        />
                    </PopoverTrigger>
                    <PopoverContent>
                        <PopoverArrow />
                        <PopoverCloseButton />
                        <PopoverHeader>Position {position}</PopoverHeader>
                        <PopoverBody>
                            { props.mode == "hplc" ?
                                <HplcSampleInfo/>:
                                <BatchSampleInfo/>
                            }
                        </PopoverBody>
                    </PopoverContent>
                    </Popover>
                </Stack>
            ))}
          </HStack>
          </CardBody>
      </Card>
      </>)
  }
